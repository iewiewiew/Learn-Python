# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/2 8:03
@description  Python的内置变量
1、vars()函数作为python的一个内置函数，以字典的形式返回当前模块中所有内置变量及其值，从上面结果可以看到，hello.py中包含有__name__、__doc__、__package__、__loader__等变量，其中__name__的值为'__main__'。
2、__doc__在函数里的介绍'''this is function1 usage'''会存储到函数function1的__doc__内置变量里
3、__name__的值为__main__或者脚本自身的名字
4、__file__用来打印当前程序所在的绝对位置
"""


def function1():
    '''this is function1 usage 说明文档'''
    print("this is function1")


if __name__ == '__main__':
    print("==========print(vars()：获取前模块中所有内置变量及其值)==============")
    print(vars())
    print("\n" + "==========print(__name__：获取到函数的名称)============")
    print(__name__)
    print("\n" + "==========print(__doc__：获取到注释内容)=============")
    print(__doc__)
    print("\n" + "==========print(__file__：获取到当前的文件路径)============")
    print(__file__)
    print("\n" + "==========print(function1.__doc__)===：获取到函数的注释内容")
    print(function1.__doc__)
