# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/9/2 07:56
@description  conftest

内置插件，就是内部_pytest这个目录下的模块（.\Python37\Lib\site-packages\_pytest）
外部插件，就是你安装的第三方插件
conftest.py，这个可以理解成框架的固定写法，把hook或者fixture写在这个文件里，就会自动去调用，文件可以作用于同级以及以下的模块。
一般可以把登陆授权的接口放到 conftest.py
"""

import time
import pytest


@pytest.fixture()
def demo_fixture():
    print("测试conftest，这是fixture函数输出")


# 注册自定义参数到配置对象
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=['这个env的默认值说明'], help="将命令行参数 '--env' 添加到 pytest 配置中")
    parser.addoption("--hostip", action="store", default="127.0.0.1", help="host ip address")


# 从配置对象中读取自定义参数的值
@pytest.fixture(scope="session")
def get_param(request):
    config_param = {}
    config_param['env'] = request.config.getoption("--env")
    config_param['hostip'] = request.config.getoption("--hostip")
    return config_param


# 从配置对象中读取 env 的值
@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption('--env')


# 将自定义参数的值打印出来
@pytest.fixture(autouse=True)
def suite_1(env):
    print('\n --env的值：', env)


# 收集测试结果
def pytest_terminal_summary(terminalreporter):
    _PASSED = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    _ERROR = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    _FAILED = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    _SKIPPED = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    _TOTAL = terminalreporter._numcollected
    _TIMES = time.time() - terminalreporter._sessionstarttime
    print(f"用例总数: {_TOTAL}")
    print(f"异常用例数: {_ERROR}")
    print(f"失败用例数: {_FAILED}")
    print(f"跳过用例数: {_SKIPPED}")
    print("用例执行时长: %.2f" % _TIMES + " s")

    try:
        _RATE = _PASSED / _TOTAL * 100
        print("用例成功率: %.2f" % _RATE + " %")
    except ZeroDivisionError:
        print("用例成功率: 0.00 %")
