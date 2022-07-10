# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/2 13:41
@description  ES 基本操作
"""

import requests


# 创建索引
def create_index():
    url = 'http://127.0.0.1:9200/person'
    json = {
        "settings": {
            "number_of_shards": 6,
            "number_of_replicas": 2
        }
    }
    resp = requests.put(url=url, json=json)

    print(resp.json())


# 删除索引
def delete_index():
    url = 'http://127.0.0.1:9200/person'
    resp = requests.delete(url=url)
    print(resp.json())


# 创建文档
def create_doc():
    url = 'http://127.0.0.1:9200/person/_doc/1'
    json = {
        "name": "wei",
        "age": 30
    }
    resp = requests.post(url=url, json=json)
    print(resp.json())


# 更新文档
def update_doc():
    url = 'http://127.0.0.1:9200/person/_doc/1'
    json = {
        "name": "weiwei",
        "age": 8888
    }
    resp = requests.post(url=url, json=json)
    print(resp.json())


# 删除文档
def delete_doc():
    url = 'http://127.0.0.1:9200/person/_doc/1'
    resp = requests.delete(url=url)
    print(resp.json())


if __name__ == '__main__':
    # create_index()
    # delete_index()
    # create_doc()
    # update_doc()
    delete_doc()
