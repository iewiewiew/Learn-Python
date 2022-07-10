# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/8/9 22:30
@description  typing 模块
python 是一门弱类型的语言，使用过程不用过多关注变量的类型，但是同时也带来了可读性问题，有时候自己都不知道传入的是什么参数。因此在 python3.5之后，引入了 typing 模块。
作用：
类型检查，提示运行时出现参数和返回值类型不对的情况；
作为开发文档附加说明，方便使用函数时传入和返回正确的参数，利于开发效率；
该模块 不会影响程序的运行，不会报错，但是会有提示。

typing 模块是 Python 3.5 引入的一个模块，主要用于指定变量、函数参数和函数返回值的类型。在 typing 模块中，有三个常用的类型：Any、Union 和 Text。
Any 类型：Any 表示任意类型，可以用于表示变量、函数参数或函数返回值的类型不确定或不限制的情况。使用 Any 类型可以使代码更加灵活，但也会降低代码的类型安全性。
Union 类型：Union 表示多种类型中的任意一种，可以用于表示变量、函数参数或函数返回值可以是多种类型的情况。使用 Union 类型可以使代码更加灵活，但也会增加代码的复杂性。
"""

from typing import List, Text, Any


def demo(num: int, string: str) -> List[int or str]:
    print(num, string)


def demo2(param: Text) -> Text:
    print(param.upper())


def demo3(param: Any) -> Any:
    print(param)


if __name__ == '__main__':
    demo(123, 'wei')
    demo2('Abc')
    demo3(11)
