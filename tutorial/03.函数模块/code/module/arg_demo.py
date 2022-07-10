# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/6 10:16
@description  sys 模块：在运行 Python 脚本文件时传递参数，sys 模块是一个内置模块，它使我们能够使用一些变量和函数在任何平台上与 Python 解释器进行交互。
"""

import sys


def arg_demo():
    """
    执行脚本: python arg_demo.py a b c
    """
    n = len(sys.argv)
    script_name = sys.argv[0]
    print("脚本名称: ", script_name)
    for i in range(1, n):
        print(f"第 {i} 个参数: {sys.argv[i]}")


if __name__ == '__main__':
    arg_demo()
