# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/15 19:21
@description  魔术方法

在 Python 中，所有以 "__" 双下划线包起来的方法，都统称为"魔术方法"。魔术方法可以将复杂的逻辑封装成简单的方法。
"""


class User(object):
    pass


if __name__ == '__main__':
    print(dir(User()))
