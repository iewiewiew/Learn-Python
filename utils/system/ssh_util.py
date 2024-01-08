# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/5 10:25
@description  封装 SSH 相关操作
"""

import paramiko
from pathlib import Path
import stat
import os
import logging


class SSHConnection:
    def __init__(self, host, user, password, port=22, mylogger=None):
        self._host = host
        self._user = user
        self._password = password
        self._port = port
        self._transport = None
        self._sftp = None
        self._client = None
        self.mylogger = mylogger
        self.connect()

    def connect(self):
        # 密钥方式
        # private = paramiko.RSAKey.from_private_key_file('/tmp/.ssh/tmp.pem')
        # transport = paramiko.Transport((self._host, self._port))
        # transport.connect(username=self._user, pkey=private)

        # 密码连接方式(通过Transport连接，或者通过SSHClient连接)
        # transport 一种加密的会话，会创建一个加密通道
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._user, password=self._password)
        self._transport = transport
        self._sftp = transport.open_sftp_client()

    def exec_cmd(self, commands: list) -> list:
        """
        :param commands: 待执行命令，支持list
        :return: 执行状态
        """
        # 实例化SSHClient
        if not self._client:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport

        status = []
        for cmd in commands:
            stdin, stdout, stderr = self._client.exec_command(cmd)
            self.writer(f"start run command: {cmd}")
            while True:
                err, out = stderr.readline().strip(), stdout.readline().strip()
                if not (out or err):
                    break
                if out:
                    self.writer(out)
                if err:
                    self.writer(err, level='error')
            status.append(stdout.channel.recv_exit_status())
        return status

    def remote_path_isdir(self, remote_path):
        """
        检查一个远程路径是否为目录
        :param remote_path:
        :return:
        """

        attr = self._sftp.lstat(self.normpath(remote_path))
        return stat.S_ISDIR(attr.st_mode)

    def check_remote_path(self, remote_path, is_mkdir=False):
        """
        判断目标机器路径是否存在
        :param remote_path:
        :param is_mkdir: 若为True，则会创建此路径
        :return:
        """

        remote_path = self.normpath(remote_path)
        try:
            self._sftp.lstat(remote_path)
            return True
        except FileNotFoundError:
            if is_mkdir:
                self._sftp.mkdir(remote_path)
            else:
                return False

    @staticmethod
    def check_or_mkdir_local_path(local_path, is_mkdir=True):
        """
        判断目录是否存在，如果不存在则创建
        :param local_path:
        :param is_mkdir:
        :return:
        """
        if isinstance(local_path, Path):
            local_path = str(local_path)
        if not os.path.exists(local_path) and is_mkdir:
            os.makedirs(local_path)

    def writer(self, message, level=None):
        """
        自定义写入log文件方法，同时支持logger或文件对象
        :param message:
        :param level:
        :return:
        """
        if self.mylogger:
            if isinstance(self.mylogger, logging.Logger):
                if not level:
                    self.mylogger.info(message)
                elif level == 'error':
                    self.mylogger.error(message)
                else:
                    self.mylogger.warning(message)
            else:
                self.mylogger.write(message)
        else:
            print(message)

    def get(self, remote_path, local_path):
        """
        下载文件或目录
        :param remote_path: 目标机器路径（注意路径反斜杠问题会报错）
        :param local_path:  本地路径
        :return:
        """
        if not self._sftp:
            # 创建一个已连通的sftp client
            # self._sftp = paramiko.SFTPClient.from_transport(self._transport)
            self._sftp = self._transport.open_sftp_client()

        if not self.check_remote_path(remote_path):
            self.writer(f"路径不存在：{remote_path}", level='error')
            return False

        local_path, remote_path = Path(local_path), Path(remote_path)

        def find_files(remote_path, local_path):
            for sftp_attr in self._sftp.listdir_attr(self.normpath(remote_path)):
                filename = sftp_attr.filename
                if filename.startswith('.'):  # 过滤隐藏文件
                    continue

                local_dir, remote_dir = local_path.joinpath(filename), remote_path.joinpath(filename)

                # 若为目录，则递归调用
                if stat.S_ISDIR(sftp_attr.st_mode):  # st_mode判断文件类型（目录还是文件）
                    local_dir.mkdir(parents=True, exist_ok=True)  # parents为True支持多级创建，exist_ok 存在就不创建
                    find_files(remote_dir, local_dir)
                else:
                    local_dir.parent.mkdir(parents=True, exist_ok=True)
                    self._sftp.get(self.normpath(remote_dir), self.normpath(local_dir))
                    self.writer(f"download file {remote_dir} -> {local_dir} successful!")

        # 下载目录
        if self.remote_path_isdir(remote_path):
            find_files(remote_path, local_path)

        # 下载单个文件，如果没有设置本地文件名，默认为远程路径中的名字
        else:
            if local_path.is_dir():
                local_path.mkdir(parents=True, exist_ok=True)
                local_path = local_path.joinpath(remote_path.name)
            else:
                local_path.parent.mkdir(parents=True, exist_ok=True)
            self._sftp.get(self.normpath(remote_path), self.normpath(local_path))
            self.writer(f"download file {remote_path} -> {local_path} successful!")

        return True

    def put(self, local_path, remote_path):
        if not self._sftp:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)

        local_path, remote_path = Path(local_path), Path(remote_path)

        if local_path.is_dir():
            for path in local_path.rglob('[!.]*'):
                # 拼接远程路径，relative_to获取相对路径
                remote = remote_path.joinpath(path.relative_to(local_path))

                if path.is_file():
                    self.check_remote_path(remote.parent, is_mkdir=True)  # 目标机器上不存在此路径需要创建
                    self._sftp.put(self.normpath(path), self.normpath(remote))
                    self.writer(f"upload the file {path} successful!")

        # 上传单个文件
        else:
            self.check_remote_path(remote_path.parent, is_mkdir=True)
            if self.remote_path_isdir(remote_path):  # 若远程路径是一个目录，就将本地文件名作为默认名字
                remote_path = remote_path.joinpath(local_path.name)
            self._sftp.put(self.normpath(local_path), self.normpath(remote_path))
            self.writer(f"upload the file {local_path} successful!")

        return True

    def close(self):
        if self._client:
            self._client.close()
        if self._transport:
            self._transport.close()
        if self._sftp:
            self._sftp.close()
        self._client, self._transport, self._sftp = None, None, None

    @staticmethod
    def normpath(path):
        """
        由于windows和linux操作系统不同，路径格式会出现不统一的情况，反斜杠不处理的话会出现很多问题
        替换windows路径中的\
        :param path:
        :return:
        """
        if isinstance(path, Path):
            path = str(path)
        return path.replace('\\', '/')

    def __del__(self):
        self.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    user = 'root'
    password = 'root'
    demo = SSHConnection(host, user, password)
    res = demo.exec_cmd(['ls -al'])
