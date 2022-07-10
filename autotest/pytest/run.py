# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/15 10:18
@description  运行pytest测试用例
"""


import os
import pytest


def run():
    # pytest.main()
    pytest.main(['--alluredir', './report/allure/tmp'])
    os.system(r"allure generate ./report/allure/tmp -o ./report/allure/html --clean")
    os.system(f"allure serve ./report/allure/tmp -p 8899")


if __name__ == '__main__':
    run()
