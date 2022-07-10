# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/15 23:44
@description  配置文件管理
"""

import configparser
import os
from os.path import dirname


def cfg_demo():
    cfgpath = os.path.dirname(dirname(os.path.realpath(__file__))) + "\\testdata\\cfgdemo.ini"

    # 创建管理对象
    conf = configparser.ConfigParser()

    # 读 ini 文件
    conf.read(cfgpath, encoding="utf-8")  # python3

    # conf.read(cfgpath)  # python2

    # 获取所有的 section
    sections = conf.sections()

    print(sections)  # 返回 list

    items = conf.items('section0')
    print(items)  # list 里面对象是元祖


if __name__ == '__main__':
    cfg_demo()
