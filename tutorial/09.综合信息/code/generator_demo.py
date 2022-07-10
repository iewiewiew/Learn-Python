# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/10 11:14
@description  生成器

生成器
生成器定义：一边循环一边计算的机制，称为生成器（generator）。生成器（generator）也是一种迭代器，在每次迭代时返回一个值，直到抛出 StopIteration 异常。
生成器作用：列表所有数据都在内存中，如果有海量数据的话将会非常耗内存。如：仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。如果列表元素按照某种算法推算出来，那我们就可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的list，从而节省大量的空间。
"""


# 创建生成器方式1：把一个列表生成式的[]改成()，就创建了一个generator
# l是一个list，而g是一个generator
def generator_demo():
    l = [x * x for x in range(10)]
    print(l)

    g = (x * x for x in range(10))

    print(g)  # 打印的是一个对象

    print('x =', next(g))
    print('x =', next(g))
    print('x =', next(g))

    print('y =', g.__next__())
    print('y =', g.__next__())
    print('y =', g.__next__())

    for i in g:
        print('z =', i)

    g.close()  # 关闭生成器


# 创建生成器方式2：yield
def yield_demo():
    for i in range(10):
        yield i


def yield_demo_test():
    yie = yield_demo()

    print('x =', next(yie))
    print('x =', next(yie))
    print('x =', next(yie))

    print('y =', yie.__next__())
    print('y =', yie.__next__())
    print('y =', yie.__next__())

    for i in yie:
        print('z =', i)


if __name__ == '__main__':
    # generator_demo()
    yield_demo_test()
