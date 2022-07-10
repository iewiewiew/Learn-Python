# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/16 16:47
@description  日志工具类
"""

import logging
import logging.handlers

from utils import get_project_root


class Logging:
    def __init__(self):
        # log文件存储路径
        self._log_filename = get_project_root("Learn-Python") + "\\autotest\\pytest\\logs\\"

        '''
        %(levelno)s: 打印日志级别的数值
        %(levelname)s: 打印日志级别名称
        %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s: 打印当前执行程序名
        %(funcName)s: 打印日志的当前函数
        %(lineno)d: 打印日志的当前行号
        %(asctime)s: 打印日志的时间
        %(thread)d: 打印线程ID
        %(threadName)s: 打印线程名称
        %(process)d: 打印进程ID
        %(message)s: 打印日志信息
        '''
        # 日志信息输出格式
        self._formatter = logging.Formatter('%(asctime)s - %(process)d - '
                                            '%(pathname)s - %(levelname)s: %(message)s')
        # 创建一个日志对象
        self._logger = logging.getLogger()
        # 设置控制台日志的输出级别: 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
        self._logger.setLevel(logging.INFO)  # 大于info级别的日志信息都会被输出
        self.set_console_logger()
        self.set_file_logger()

    def set_console_logger(self):
        '''设置控制台日志输出'''
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self._formatter)
        self._logger.addHandler(console_handler)

    def set_file_logger(self):
        '''设置日志文件输出'''
        formatter = logging.Formatter('%(asctime)s - %(process)d - '
                                      '%(pathname)s - %(levelname)s: %(message)s')
        # 将输出日志信息保存到文件中
        file_handler = logging.handlers.RotatingFileHandler(
            self._log_filename, maxBytes=10485760, backupCount=5, encoding="utf-8")
        file_handler.setFormatter(self._formatter)
        self._logger.addHandler(file_handler)

    def get_logger(self):
        return self._logger


if __name__ == '__main__':
    logger = Logging().get_logger()
    logger.info("12345")
    logger.debug("12345")
    logger.warning("12345")
    logger.error("12345")
