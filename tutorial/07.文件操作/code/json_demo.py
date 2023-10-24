#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2021/7/25 9:40
@description 读写 json
"""

import re
import json
import jsonpath
from utils.path_util import get_file_path


def write_json():
    """
    写入 json
    """
    data = {"name": "wei", "job": "tester"}
    with open(get_file_path() + 'data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def read_json():
    """
    json 有四个方法：dumps 和 loads、dump 和 load。
    其中，dumps 和 loads 是在内存中转换（python 对象和 json 字符串之间的转换），而 dump 和 load 则是对应于文件的处理。
    """
    with open(get_file_path() + 'data.json', 'r') as f:
        data = json.load(f)
        print(data)


def jsonpath_demo():
    filePath = '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/tmp.json'

    # fliePath = get_file_path() + 'jsonpath.json'
    file = json.load(open(filePath, 'r', encoding="utf-8"))
    # print(file)

    # author = jsonpath.jsonpath(file, '$.store.book[*].author')
    # print(author)

    # author2 = jsonpath.jsonpath(file, '$..author')
    # print(author2)

    # str = json.dumps(file)
    # str = re.findall(r'\"store\":\".*?\"', file)
    # print(str)

    groups_id = jsonpath.jsonpath(file, '$.groups.[*].id')
    print(groups_id)


if __name__ == '__main__':
    # write_json()
    # read_json()
    jsonpath_demo()
