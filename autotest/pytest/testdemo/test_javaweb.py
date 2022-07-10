# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/16 10:33
@description  pytest测试JavaWeb接口
"""

import pytest
import requests


class TestCase:
    def test_list(self):
        url = "http://127.0.0.1:9999/demo/list"
        response = requests.get(url=url)
        print("响应内容：{}  响应码：{}".format(response.text, response.status_code))

    def test_update(self):
        headers = {
            "Content-Type": "application/json",
        }
        url = "http://127.0.0.1:9999/demo/update"
        json = {
            "id": "1",
            "username": "python",
            "password": "123456",
        }
        response = requests.post(headers=headers, url=url, json=json)
        print("响应内容：{}  响应码：{}".format(response.text, response.status_code))
        assert "true" == response.text, "报错"


if __name__ == '__main__':
    pytest.main()
