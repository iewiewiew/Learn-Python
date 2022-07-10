# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/21 08:36
@description  pytest_addoption 注册参数

pytest_addoption 的含义是，接收命令行选项--env 选项的值，存到 environment 变量中，如果不指定命令行选项，environment 变量默认值是 test。
将上面代码也放入 conftest.py 中，并修改 env 函数，将 os.path.join 中的"test"替换为 request.config.getoption("environment")，这样就可以通过命令行选项来控制读取的配置文件了。
pytest --env test tests/test_in_theaters.py

parser.addoption() 参数说明：
name：自定义命令行参数的名字，可以是："foo"， "-foo" 或 "--foo"；
action：在命令行中遇到此参数时要采取的基本操作类型；
nargs：应该使用的命令行参数的数量；
const：某些操作和nargs选择所需的常量值；
default：如果参数不在命令行中，则生成的默认值。
type：命令行参数应该转换为的类型；
choices：参数允许值的容器；
required：命令行选项是否可以省略（仅可选）；
help：对参数作用的简要说明；
metavar：用法消息中参数的名称；
dest：要添加到 parse_args() 返回的对象中的属性的名称；
"""

import pytest


def test_addoption():
    print('测试 addoption')


if __name__ == '__main__':
    # 使用参数
    pytest.main(['-s', '--env=test'])
    # pytest.main(['-s', '--env=test', '--env=dev'])
