#!/usr/bin/env python
# !coding:utf-8

"""
@author      weimenghua
@time        2020/9/19 12:29
@description 迭代器

1、迭代器
迭代器定义：迭代器(Iterator)是访问集合内元素的一种方式，提供了一种遍历序列对象的方法。一个类（对象）只要含有__iter__、__next__两个方法，就将其称为迭代器。
迭代器作用：迭代器最核心的功能就是可以通过__next__方法的调用来返回下一个值。而这个值不是从已有的数据中读取的，而是通过程序按照一定的规则生成的。这也就意味着我们可以不再依赖一个现存的数据集合来存放数据，而是边用边生成，这样的好处就是可以节省大量的内存空间。

2、可迭代对象
一个对象只要含有__iter__方法，就将其称为可迭代对象。
Python可迭代对象有str（字符串）、list（列表）、tuple（元组）、dirt（字典）、set（集合）等。

3、总结
1.可迭代对象不一定是迭代器。
2.迭代器一定是可迭代对象。
3.容器类型（str list tuple dict set）是可迭代对象但不是迭代器。
"""

import sys
from typing import Iterable, Iterator


# 定义一个迭代器
class IterDemo:
    def __iter__(self):
        self.a = 1
        return self  # __iter__ 方法返回了实例本身 self，也就是说返回了一个迭代器，所以 IterDemo 的实例 iterDemo 也是一个「可迭代对象」

    def __next__(self):
        x = self.a
        self.a += 1
        if self.a == 10:
            raise StopIteration()  # 异常用于标识迭代的完成，防止出现无限循环的情况
        return x


def iter_demo():
    iterDemo = IterDemo()
    it = iter(iterDemo)  # 创建迭代器对象

    print('x = ', it.__next__())  # 输出迭代器的下一个元素
    print('x = ', it.__next__())  # 输出迭代器的下一个元素
    print('x = ', it.__next__())  # 输出迭代器的下一个元素

    print('y = ', next(it))  # 输出迭代器的下一个元素
    print('y = ', next(it))  # 输出迭代器的下一个元素
    print('y = ', next(it))  # 输出迭代器的下一个元素

    for i in it:
        print('z = ', i)


# isinstance()检查对象是否是 类/子类 的实例
def isinstanc_demo():
    lisTest = [1, 2, 3]  # 可迭代的
    lisTest1 = 1  # 不可迭代的
    print("判断是否是可迭代的对象：", isinstance(lisTest, Iterable))  # Iterable（可迭代对象）
    print("判断是否是迭代器：", isinstance(lisTest, Iterator))       # Iterator（迭代器）
    print("判断是否是迭代器：", isinstance(IterDemo(), Iterator))    # Iterator（迭代器）


# 字符串迭代器
def demo2():
    strTest = 'abc'
    it = iter(strTest)  # 创建迭代器对象
    print("x =", next(it))  # 输出迭代器的下一个元素
    print("x =", next(it))  # 输出迭代器的下一个元素
    print("x =", next(it))  # 输出迭代器的下一个元素


# 列表迭代器
def demo1():
    listTest = ['a', 'b', 'c']
    it = iter(listTest)  # 创建迭代器对象
    print("x =", next(it))  # 输出迭代器的下一个元素
    print("x =", next(it))  # 输出迭代器的下一个元素
    print("x =", next(it))  # 输出迭代器的下一个元素


# 元组迭代器
def demo3():
    tupleTest = ('a', 'b', 'c')
    it = iter(tupleTest)  # 创建迭代器对象
    print("x =", next(it))  # 输出迭代器的下一个元素
    print("x =", next(it))  # 输出迭代器的下一个元素
    print("x =", next(it))  # 输出迭代器的下一个元素


def demo4():
    listTest = ['a', 'b', 'c']

    # 迭代遍历
    it = iter(listTest)  # 创建迭代器对象
    print('x= ', it.__next__())

    print('y=', next(it))

    for i in it:
        print("z =", i)  # 输出迭代器的下一个元素

    # 正常遍历
    for j in listTest:
        print("j =", j)


def demo5():
    listTest = ['a', 'b', 'c']
    it = iter(listTest)  # 创建迭代器对象
    while True:
        try:
            print("y =", next(it))
        except StopIteration:  # 异常用于标识迭代的完成，防止出现无限循环的情况
            sys.exit()


if __name__ == '__main__':
    iter_demo()
    isinstanc_demo()
    demo4()
