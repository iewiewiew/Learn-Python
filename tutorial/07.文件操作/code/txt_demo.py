#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2021/7/25 9:40
@description 读写 txt
"""


def write_txt():
    """
    写入 txt
    """
    with open('../files/data.txt', 'w') as f:
        # f.write("我是 txt 啊")
        for i in range(10000):
            f.write(str(i))


def read_txt():
    """
    读取 csv
    """
    with open('../../../files/data.txt', 'r') as f:
        str = f.read()
        print(str)


if __name__ == '__main__':
    write_txt()
    # read_txt()
