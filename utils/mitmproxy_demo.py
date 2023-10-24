# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/14 18:17
@description  Mitmproxy 开源的中间人代理工具，官网：https://mitmproxy.org/
"""

import csv
from mitmproxy import http


class RequestRecorder:
    def __init__(self):
        self.records = []

    def request(self, flow: http.HTTPFlow):
        if "www.demo.com" in flow.request.url:
            # 获取请求的 URL、方法、请求头和请求参数
            url = flow.request.url
            method = flow.request.method
            headers = dict(flow.request.headers)
            params = dict(flow.request.query or {})
            record = {
                "URL": url,
                "Method": method,
                "Headers": headers,
                "Params": params,
            }
            self.records.append(record)

    def done(self):
        # 保存记录到 CSV 文件
        with open("/Users/menghuawei/PycharmProjects/Learn-Python/.gitee/testdata/api_requests.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["URL", "Method", "Headers", "Params", "Response"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for record in self.records:
                writer.writerow(record)


addons = [
    RequestRecorder()
]


"""
打开浏览器，并将代理地址设置为 http://localhost:8080
运行脚本：mitmdump -s mitmproxy_demo.py
"""
