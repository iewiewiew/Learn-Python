# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/24 13:36
@description

os.sep 是 Python 中用于表示系统路径分隔符的变量，通常表示斜杠 /。
os.sep.join 是一个函数，用于将多个字符串按照 os.sep 分隔，并返回一个新的字符串。
"""
import os

if __name__ == '__main__':
    path1 = "/aa/bb"
    path2 = "/cc/dd"
    print(os.sep)
    print(os.sep.join(path1.split("/")))
    print(path1.split("/"))
    print(os.sep.join([path1, path2]))

