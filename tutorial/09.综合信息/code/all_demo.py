# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/9 13:45
@description  小技巧
"""


def demo():
    n1, n2, n3 = input("enter a number: ").split()
    print(n1, n2, n3)


def demo1(size, color, price):
    """ 有多个 and 条件时使用 all()，当我们有多个 or 条件时使用 any() """
    conditions = [
        size == "lg",
        color == "blue",
        price < 100,
    ]

    if all(conditions):
        print("满足条件")


def demo2(size, color, price):
    """ 有多个 and 条件时使用 all()，当我们有多个 or 条件时使用 any() """
    conditions = [
        size == "lg",
        color == "blue",
        price < 100,
    ]

    if any(conditions):
        print("满足条件")


if __name__ == '__main__':
    # demo()
    # demo1("lg", "blue", 99)
    demo2("lg", "blue", 99)