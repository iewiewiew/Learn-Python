#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2021/7/25 8:20
@description list 数组：列表都可以进行的操作包括索引，切片，加，乘，检查成员

在 Python 中，列表切片 (slice) 是一种用于访问列表中特定部分的语法。切片使用方括号和冒号来指定要提取的子列表的起始和结束位置。其中，起始位置用整数 i 表示，结束位置用整数 i+k-1 表示，其中 k 是列表的长度。
"""
import os


def list_demo():
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c', 'd', 'e']
    list3 = ['red', 'green', 'blue', 'yellow', 'white']
    list4 = ['a', 'b', 'c', 2022, 2023]

    parent_dir, file_name = os.path.split("/aa/bb/cc/demo.py")

    print('第一个：' + list3[0])
    print('倒数第一个：' + list3[-1])
    print("从第三个到结束'%s'" % list3[2:])
    print("主目录：%s 子目录：%s" % (parent_dir, file_name))
    print("主目录：'%s'" % os.path.split("/aa/bb/cc/demo.py")[0])
    print("子目录：'%s'" % os.path.split("/aa/bb/cc/demo.py")[1])
    print("提取文件名称：'%s'" % os.path.split("/aa/bb/cc/demo.py")[1][:-3])


# 删除列表内的重复元素
def list_norepeat():
    test_list = [1, 3, 5, 2, 4, 6, 1, 6]
    res = []
    for i in test_list:
        if i not in res:
            res.append(i)
    print(res)


if __name__ == '__main__':
    list_demo()
