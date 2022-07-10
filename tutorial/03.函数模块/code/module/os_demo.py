# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/2 8:22
@description  os 模块
"""

import os
import sys


def os_demo():
    curPath = os.path.abspath('../../..')
    print("当前路径：" + curPath)

    lastPath = os.path.abspath('../../../../autotest')
    print("上一级目录：" + lastPath)

    # 如果是 posix，说明系统是 Linux、Unix 或 Mac OS X，如果是 nt，就是 Windows 系统
    print('操作系统：' + os.name)

    print('当前方法名：' + sys._getframe().f_code.co_name)


if __name__ == '__main__':
    os_demo()
