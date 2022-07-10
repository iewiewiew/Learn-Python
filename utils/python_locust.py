# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/5/29 18:27
@description  locust 性能测试
"""

from locust import HttpUser, task


"""
执行脚本：locust -f python_locust.py
访问地址：http://127.0.0.1:8089/
"""

class LocustTest(HttpUser):

    host = "http://www.baidu.com"  # host

    def on_start(self):
        print("start working")

    @task(1)
    def locust_test(self):
        header = {"Content-Type": "application/json"}
        data = {}
        print("正在请求！！！")
        self.client.post("/", data=data, headers=header)
