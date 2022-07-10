# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 21:12
@description  ddt：数据驱动
数据驱动原理：
1.测试数据为多个字典的list类型
2.测试类前加修饰@ddt.ddt
3.case前加修饰@ddt.data()
4.运行后用例会自动加载成三个单独的用例
"""

import ddt
import unittest
from utils import get_project_root


testData = [{"username": "demo1", "password": "123"},
            {"username": "demo2", "password": "456"}]
@ddt.ddt
class Test(unittest.TestCase):
    @ddt.data(*testData)
    def test_01(self, data):
        print("测试数据 %s" % testData)
        print(data['username'], data['password'])

    """
    @data([a, b], [c, d])
    如果没有 @unpack，那么[a, b]，当成一个参数传入用例运行
    如果有 @unpack，那么[a, b]，被分解开，按照用例中的两个参数传递
    """
    @ddt.data([1, 2], [3, 4])
    @ddt.unpack
    def test_02(self, value):
        print(value)

    path1 = get_project_root("Learn-Python") + "\\autotest\\selenium\\testdata\\unitest_data1.json"
    @ddt.file_data(path1)
    def test_03(self, a, b, c):
        print(a, b, c)

    path2 = get_project_root("Learn-Python") + "\\autotest\\selenium\\testdata\\unitest_data2.json"
    @ddt.file_data(path2)
    def test_03(self, data, result):
        print(data, result)


if __name__ == '__main__':
    # todo：运行这几个方法异常
    unittest.main()
