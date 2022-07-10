# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/3 12:46
@description  HTMLTestRunner：测试报告
"""

import unittest
import HTMLTestRunner
from utils import get_project_root


class Test(unittest.TestCase):
    def test_01(self):
        print('---用例01---')

    def test_02(self):
        print('---用例02---')

    def test_03(self):
        print('---用例03---')


if __name__ == '__main__':
    # todo：没有生成测试报告

    # 创建测试套件
    suite = unittest.TestSuite()
    # 测试用例加入到测试套件中
    suite.addTests([Test('test_01'), Test('test_02'), Test('test_03')])
    report_path = get_project_root("Learn-Python") + "\\autotest\\unitest\\report\\report.html"
    print("报告路径 " + report_path)
    # 打开报告
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # 执行用例
    runner.run(suite)
    # 关闭报告
    # fp.close()
