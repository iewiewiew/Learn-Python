#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2022/2/14 22:22
@description copy模块：复制

直接赋值：其实就是对象的引用（别名）。
浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
深拷贝(deepcopy)：copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
"""


import copy


def shallow_copy():
    # 浅拷贝, a和b是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。
    a = {1: [1, 2, 3]}
    b = a.copy()
    print("a=", a)
    print("b=", b)
    a[1].append(4)
    print("copy a=", a)
    print("copy b=", b)


def deep_copy():
    # 深度拷贝, a和b完全拷贝了父对象及其子对象，两者是完全独立的。
    a = {1: [1, 2, 3]}
    b = copy.deepcopy(a)
    print("a=", a)
    print("b=", b)
    a[1].append(4)
    print("deepcopy a=", a)
    print("deepcopy b=", b)


if __name__ == '__main__':
    # shallow_copy()
    deep_copy()
