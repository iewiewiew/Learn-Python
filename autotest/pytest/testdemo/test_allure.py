#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2022/2/12 11:51
@description @allure：allure测试报告
"""

import allure
import pytest
import os

"""
在该模块的当前路执行测试用例：pytest test_allure.py --alluredir ./allure
在allure目录下打开测试报告（自动打开浏览器）：allure serve ./allure
"""


class Test_case:
    @allure.step(title="步骤1")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.testcase("http://www.baidu.com/", "地址（百度）")
    def test_case1(self):
        allure.attach("用例1的描述内容", "用例1的描述标题")
        print("执行用例1")

    @allure.step(title="步骤2")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("http://www.sohu.com/", "地址（搜狐）")
    def test_case2(self):
        allure.attach("用例2的描述内容", "用例2的描述标题")
        print("执行用例2")

    @allure.step(title="步骤3")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("http://www.sina.com.cn/", "地址（新浪）")
    def test_case3(self):
        allure.attach("用例3的描述内容", "用例3的描述标题")
        print("执行用例3")

    @allure.step(title="步骤4")
    def test_case4(self):
        allure.attach("用例4的描述内容", "用例4的描述标题")
        print("执行用例4")


if __name__ == '__main__':
    # pytest.main()
    # pytest.main(["-sv", "--html=./reports/report.html"])
    # pytest.main(['--alluredir', './allure'])
    # os.system('allure generate -c -o ./allure ./allure')
    # os.system(f"allure serve ./allure -p 5566")

    pytest.main(['-s', '-v',
                 '--alluredir', './report/tmp', "--clean-alluredir"])
    os.system(r"allure generate ./report/tmp -o ./report/html --clean")
    # os.system(f"allure serve ./report/tmp -h 127.0.0.1 -p 9999")


