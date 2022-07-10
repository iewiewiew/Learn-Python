#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2020/9/20 8:38
@description JavaWeb接口增删改查
"""


import requests
import sys


def getlist(url):
    resp = requests.get(url)
    print(sys._getframe().f_code.co_name + "响应：" + resp.text)


def add(url, json):
    resp = requests.post(url=url, json=json)
    print(sys._getframe().f_code.co_name + "响应：" + resp.text)


def update(url, json):
    resp = requests.post(url=url, json=json)
    print(sys._getframe().f_code.co_name + "响应：" + resp.text)


if __name__ == '__main__':
    url = 'http://127.0.0.1:9999/demo'
    getlist(url)

    url1 = 'http://localhost:9999/demo/add'
    json1 = {
        "id": "1",
        "username": "zyx123",
        "password": "123456"
    }
    add(url1, json1)

    url2 = 'http://localhost:9999/demo/update'
    json2 = {
        "id": "1",
        "username": "zhangyixing",
        "password": "123456"
    }
    update(url2, json2)
