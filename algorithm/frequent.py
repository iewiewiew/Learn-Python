#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author       weimenghua
@time         2021/5/23 8:49
@description  查找出现次数最多的元素
"""


# 查找出现次数最多的元素：使用max方法找出列表中出现次数最多的元素。
def frequent(list):
    return max(set(list), key=list.count)


if __name__ == '__main__':
    mylist = [1, 0, 2, 3, 4, 1, 5, 6, 6, 2, 2]
    print("出现次数最多的元素是:", frequent(mylist))