#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@Time        2021/10/10 9:59
@description str 和 json 转换

json 模块有四个比较重要的函数，分别是：
dump - 将 Python 对象按照 JSON 格式序列化到文件中
dumps - 将 Python 对象处理成 JSON 格式的字符串
load - 将文件中的 JSON 数据反序列化成对象
loads - 将字符串的内容反序列化成 Python 对象
"""

import json


def str2json():
    # json中内部数据需要用双引号来包围，不能使用单引号
    str = '{"name": "张艺兴" , "job": "歌手"}'
    j = json.loads(str)
    print("类型：", type(j), j)


def json2str():
    # json.dumps序列化时对中文默认使用的ascii编码，ensure_ascii=False（默认为true），将启用原来的编码形式
    str = {'name': '张艺兴', 'job': '歌手'}
    str = json.dumps(str, ensure_ascii=False)
    print("类型：", type(str), str)


if __name__ == '__main__':
    str2json()
    json2str()
