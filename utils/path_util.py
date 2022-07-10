#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2020/8/24 21:54
@description 获取路径
"""

import os
import sys
from os.path import dirname


def get_path_all():
    print("\n获取当前文件名称")
    print(__file__)
    print(os.path.realpath(__file__))
    print(os.path.realpath(sys.argv[0]))

    print("\n获取当前目录")
    print(os.path.abspath(dirname(__file__)))
    print(os.getcwd())

    print("\n获取当前目录的上一级目录")
    print(os.path.abspath(dirname(dirname(__file__))))
    print(os.path.abspath(os.path.join(os.getcwd(), "..")))

    print("\n获取当前目录的上上一级目录")
    print(os.path.abspath(dirname(dirname(dirname(__file__)))))

    print("\n")


def get_path():
    return os.path.abspath(os.path.join(os.getcwd(), ".."))


def get_project_root(projectname):
    curPath = os.path.abspath(os.path.dirname(__file__))
    if 'win32' in sys.platform:
        rootPath = curPath[:curPath.find("{}\\".format(projectname)) + len("{}\\".format(projectname))]
    elif 'linux' in sys.platform:
        rootPath = curPath[:curPath.find("{}/".format(projectname)) + len("{}/".format(projectname))]
    else:
        rootPath = curPath[:curPath.find("{}/".format(projectname)) + len("{}/".format(projectname))]
    return rootPath


def get_file_path():
    file_path = get_project_root("Learn-Python") + "files/"
    return file_path


def get_os_sep():
    """
    判断不同的操作系统的路径
    :return: windows 返回 "\", linux 返回 "/"
    """
    return os.sep


if __name__ == "__main__":
    # get_path_all()
    # print(get_path())
    # print(get_project_root("Learn-Python"))
    # print(get_file_path())
    print(get_os_sep())

