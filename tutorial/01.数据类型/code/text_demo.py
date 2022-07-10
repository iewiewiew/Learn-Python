# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/3/31 16:05
@description  Text

这是一个 Python 的类型提示 (Type Hint) 语法，用于表明函数的参数和返回值的类型。具体来说，这个语法使用了 Python 3.5 引入的类型提示功能中的两个类型：Text 和 str。
Text 类型表示文本类型，这个 Text 类型不是 Python 内置的类型，而是在一些第三方库中定义的。通常情况下，这个类型实际上就是 str 类型，只不过为了兼容 Python 2.x 中的 Unicode 和字符串类型而定义的。
str 类型表示 Python 中的字符串类型，它在 Python 内置的数据类型中非常常用，可以存储任意长度的字符序列。
因此，python (path: Text) -> Text 这个语法表示一个名为 python 的函数，它有一个名为 path 的参数，这个参数的类型为 Text，函数的返回值类型也为 Text。
"""

from typing import Text


def path_str(path: str) -> str:
    return path


def path_text(path: Text) -> Text:
    return path


if __name__ == '__main__':
    print(path_str("test"))
    print(path_text("dev"))
