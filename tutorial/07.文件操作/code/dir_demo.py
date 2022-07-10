#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2021/7/28 14:33
@description 目录操作
"""

import os
from os.path import join, getsize


def mkdir():
    """
    创建文件夹
    """

    if os.path.exists("../files/新文件夹名称"):
        print("该文件夹已存在")
    else:
        # 创建单层文件夹
        os.mkdir("../files/新文件夹名称")

    if os.path.exists("../files/第一层/第二层/第三层"):
        print("该文件夹已存在")
    else:
        # 创建多层文件夹
        os.makedirs("../files/第一层/第二层/第三层")

    # 循环创建单层文件夹
    list = ["../testdata/文件夹{}".format(i) for i in range(5)]
    for i in list:
        os.mkdir(i)


def get_size(dir):
    """
    获取某个目录下的文件大小
    """

    size = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            tmp = getsize(join(root, file))
            print('文件名：%-25s  文件大小：%-5.2fMB' % (file, tmp / 1024 / 1024))
        size += sum([getsize(join(root, name)) for name in files])
    print('%s, 合计大小：%sByte, %.2fKB, %.2fMB' % (dir, size, size / 1024, size / 1024 / 1024))


if __name__ == '__main__':
    get_size('')
