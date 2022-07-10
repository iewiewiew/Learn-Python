#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author       weimenghua
@time         2021/7/25 17:28
@description  99乘法表
"""


def nine1():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end=' ')
        print(' ')


def nine2():
    for row in range(1, 10):  # 打印行
        for col in range(1, row + 1):  # 打印列
            print('{0}*{1}={2:2d}'.format(row, col, row * col), end=' ')
        print(' ')


if __name__ == '__main__':
    nine1()
    nine2()
