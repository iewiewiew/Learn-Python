# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/5/11 14:15
@description  for
"""


def demo1():
    sum = 0
    for x in range(100):
        sum += x
    print(sum)


def demo2():
    a, b = 0, 1
    for _ in range(5):
        a, b = b, a + b
        print(a)


if __name__ == '__main__':
    demo1()
    demo2()
