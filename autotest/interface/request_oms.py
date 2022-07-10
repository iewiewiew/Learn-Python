#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2020/9/20 8:38
@description 运营平台登录接口
"""


import json
import re
import requests


host = 'https://www.demo.com/'


def login():
    path = '/loginByAjax'
    url = ''.join([host, path])
    params = {'uname': 'root', 'pwd': 'root'}
    resp = requests.get(url, params=params)

    userId = resp.json()['data']['userId']
    resp_json = resp.json()

    with open("token.json", "w") as f:
        # json.dumps将字典形式的数据转化为字符串 ; ensure_ascii=False 防止Unicode格式被转换
        response = json.dumps(resp_json, ensure_ascii=False)
        # 将响应结果写入token.json
        f.write(response)
    return resp


def get_token1():
    # login() 直接调用login()的返回值
    resp_str = str(login().json())
    token = re.findall(r"TOKEN:(.+?)'}", resp_str)
    # 将数组转换为字符串
    TOKEN = ','.join(token)
    print(TOKEN)


def get_token2():
    with open('token.json', 'r') as f:
        # str()将json转换为字符串 ; json.load()用于从json文件中读取数据
        data = str(json.load(f))
        # 正则表达式获取TOKEN
        token = re.findall(r"TOKEN:(.+?)'}", data)
        # 将数组转换为字符串
        TOKEN = ','.join(token)
        print(TOKEN)


if __name__ == '__main__':
    login()
    get_token1()
    get_token2()

