# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 11:11
@description  assert：断言
"""

import unittest


class Test(unittest.TestCase):
    def test_01(self):
        print("判断a是否存在b中")
        a = "py"
        b = "python"
        self.assertIn(a, b)

    def test_02(self):
        print("判断a是否等于b")
        a = 123
        b = 123
        self.assertEqual(a, b)

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
