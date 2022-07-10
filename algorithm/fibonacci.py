#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author       weimenghua
@time         2021/7/25 16:53
@description  斐波那契数列。递归：程序自己调用自己。
"""

import timeit
from functools import lru_cache

# functools.lru_cache 是 Python 标准库中的一个装饰器函数，用于实现缓存功能。LRU（Least Recently Used，最近最少使用）缓存是一种常见的缓存策略，它基于访问模式来保留最常用的项目，并且在缓存达到最大容量时会删除最不常用的项目。
@lru_cache(maxsize=100)
def recur_fibo(n):
    # 递归函数 输出斐波那契数列
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


if __name__ == '__main__':
    nterms = 6
    if nterms <= 0:
        print("请输入大于0的整数")
    else:
        print("斐波那契数列:")
        for i in range(nterms):
            print(recur_fibo(i))

    t1 = timeit.Timer("recur_fibo(40)", "from __main__ import recur_fibo")
    print(t1.timeit(1))
