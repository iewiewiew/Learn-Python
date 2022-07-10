# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/5/4 10:19
@description  lambda 表达式

函数可以赋值给变量
函数可以作为函数的参数
函数可以作为函数的返回值
"""


# @todo 没看明白
def demo1():
    items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
    items2 = [x ** 2 for x in range(1, 10) if x % 2]
    print(items1)
    print(items2)


def demo2():
    add = lambda x, y: x + y
    print(add(3, 4))


if __name__ == '__main__':
    # demo1()
    demo2()
