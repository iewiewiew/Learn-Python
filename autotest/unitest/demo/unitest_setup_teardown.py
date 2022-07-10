# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 11:11
@description  setup和teardown：执行用例前后
"""

import unittest


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("在所有用例前执行")

    @classmethod
    def tearDownClass(cls):
        print("在所有用例后执行")

    def setUp(self):
        print("在每条用例前执行")

    def tearDown(self):
        print("在每条用例后执行")

    def test_01(self):
        print("用例1")

    def test_02(self):
        print("用例2")

    def test_03(self):
        print("用例3")


if __name__ == '__main__':
    unittest.main()
