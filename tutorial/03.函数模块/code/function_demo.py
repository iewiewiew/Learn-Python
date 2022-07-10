# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/5/10 10:34
@description  函数
"""


# 用星号表达式来表示 args 可以接收0个或任意多个参数
def demo1(*args):
    for arg in args:
        print(arg)


def demo2(*args, **kwargs):
    for var in args:
        print(var)

    # **kwargs 用于处理带参数名的参数
    for kw in kwargs.values():
        print(kw)


if __name__ == '__main__':
    demo2(1, 2, 3, 4)

    # 不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前，否则将会引发异常。
    demo2(1, 2, c=3, d=4)
