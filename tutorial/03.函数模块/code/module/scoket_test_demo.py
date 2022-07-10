# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/11 18:32
@description  测试 socket 连接
"""

from socket import socket
import socket


def demo():
    # 1.创建套接字对象默认使用 IPv4和 TCP 协议
    client = socket()
    # 2.连接到服务器(需要指定 IP 地址和端口)
    client.connect(('127.0.0.1', 1234))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


def demo1():
    # 1、发送请求
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('www.sina.com.cn', 80))
    client.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

    # 2、接收数据
    buffer = []
    while True:
        d = client.recv(1024)
        if d:
            buffer.append(d)
        else:
            break

    data = b''.join(buffer)

    client.close()

    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))

    with open('../../../文件操作/files/demo.html', 'wb') as f:
        f.write(html)


if __name__ == '__main__':
    demo1()
