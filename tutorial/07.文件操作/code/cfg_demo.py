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


def read_cfg():
    cfgpath = os.path.dirname(dirname(os.path.realpath(__file__))) + "/files/cfgdemo.ini"

    print(cfgpath)

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


def write_cfg():
    config = configparser.ConfigParser()

    config["redis"] = {
        "host": "127.0.0.1",
        "port": "6379"
    }

    config["exec"] = {}
    config["exec"]["debug"] = "False"
    config["exec"]["node"] = "10"

    cfgpath = os.path.dirname(dirname(os.path.realpath(__file__))) + "/files/cfgdemo2.ini"
    with open(cfgpath, "w+") as f:
        config.write(f)


if __name__ == '__main__':
    # read_cfg()
    write_cfg()
