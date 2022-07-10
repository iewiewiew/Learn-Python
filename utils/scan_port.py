# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/11 13:47
@description  端口扫描
"""

import socket
from multiprocessing import Pool
from functools import partial


def scan_port(ip, port):
    try:
        """
        使用 Python 的 socket 模块创建一个 TCP/IP 套接字对象
        socket.AF_INET 是一个常量，表示使用 IPv4 地址族
        socket.SOCK_STREAM 也是一个常量，表示创建一个可靠的、面向连接的 TCP 套接字
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # 设置超时时间为1s
        result = s.connect_ex((ip, port))  # 尝试建立与远程主机的连接
        if result == 0:  # 返回值为 0，则表示连接成功
            print('[+] %d/tcp open' % port)
        s.close()
    except socket.error:
        pass


if __name__ == '__main__':
    ip = '127.0.0.1'
    start_port = 1
    end_port = 1024

    # 是在 Python 中使用多进程的上下文管理器语法，其中 Pool 是 multiprocessing 模块中的一个类，用于创建进程池。processes=10 指定了进程池中的进程数量为 10
    with Pool(processes=10) as pool:
        """
        注：没看懂
        partial(scan_port, ip)：partial 是 functools 模块中的一个函数，用于部分应用函数。在这里，它将 scan_port 函数与 ip 参数进行部分应用，创建了一个新的函数，即 scan_port(ip, port)。
        pool.map(partial(scan_port, ip), range(start_port, end_port + 1))：pool.map() 方法接受一个函数和一个可迭代对象作为参数。它将函数应用于可迭代对象的每个元素，并返回一个结果列表。在这里，我们将部分应用后的 scan_port(ip, port) 函数和端口号序列作为参数传递给 pool.map() 方法，从而并行地对每个端口执行端口扫描任务。
        """
        pool.map(partial(scan_port, ip), range(start_port, end_port + 1))
