# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 11:11
@description  skip：跳过测试用例执行
"""

import unittest


class Test(unittest.TestCase):
    @unittest.skip(reason="跳过当前用例")
    def test_01(self):
        print("判断a是否存在b中")
        a = "py"
        b = "python"
        self.assertIn(a, b)

    @unittest.skipIf(True, reason="条件为True是跳过当前测试用例")
    def test_02(self):
        print("判断a是否等于b")
        a = 123
        b = 123
        self.assertEqual(a, b)

    @unittest.skipUnless(False, reason="条件为False时跳过当前测试用例")
    def test_03(self):
        print("判断a是否等于True")
        a = True
        self.assertTrue(a)

    def test_04(self):
        print("判断a是否等于b")
        a = "py"
        b = "py"
        self.assertIs(a, b)


if __name__ == '__main__':
    unittest.main()
