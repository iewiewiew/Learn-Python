#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author       weimenghua
@time         2021/7/25 17:07
@description  冒泡排序
"""


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(arr)
    print("排序后数组:", arr)

    for i in range(len(arr)):
        print("排序后元素:", "%d" % arr[i])
