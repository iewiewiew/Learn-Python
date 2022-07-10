#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2021/8/14 8:50
@description 获取本机ip地址
"""

import socket as f
import json
from urllib.request import urlopen
import ssl


def get_hostname():
    hostname = f.gethostname()
    laptop = f.gethostbyname(hostname)
    print("你的电脑本地IP地址是：" + laptop)

    # 全局取消证书验证
    ssl._create_default_https_context = ssl._create_unverified_context
    with urlopen(r'https://jsonip.com') as fp:
        content = fp.read().decode()

    ip = json.loads(content)['ip']
    print("你的电脑公网IP地址是：" + ip)


if __name__ == '__main__':
    get_hostname()
