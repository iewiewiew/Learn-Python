# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 11:11
@description  TestSuite：测试套件
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
    # 创建测试套件
    suite = unittest.TestSuite()
    # 测试用例加入到测试套件中
    suite.addTests(Test['test_01'], Test['test_03'])
    # 执行测试用例
    run = unittest.TextTestRunner()
    run.run(suite)