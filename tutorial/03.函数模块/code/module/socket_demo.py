# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/11 18:27
@description  socket
"""

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def demo():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP 套接字
    # type=SOCK_DGRAM - UDP 套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定 IP 地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('127.0.0.1', 1234))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept 方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept 方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由 IP 和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        # 5.发送数据
        client.send(('服务端时间：' + str(datetime.now())).encode('utf-8'))
        # 6.断开连接
        client.close()


if __name__ == '__main__':
    demo()
