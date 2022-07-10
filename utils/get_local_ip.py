# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/6/19 15:45
@description  查询本机ip地址
"""

import socket


def get_host_ip():
    """查询本机ip地址"""

    _s = None
    try:
        _s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _s.connect(('8.8.8.8', 80))
        l_host = _s.getsockname()[0]
    finally:
        _s.close()

    return l_host


if __name__ == '__main__':
    print(get_host_ip())
