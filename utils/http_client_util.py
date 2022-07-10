# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/21 18:31
@description  HTTP 请求工具类
"""

import inspect
import json
import http.client
import ssl
from datetime import datetime
from urllib.parse import urlencode

from utils.decorator_all import method_decorator


class HttpClient:
    def __init__(self, host):
        # 创建了默认的 ssl.SSLContext 对象，并将 check_hostname 属性设置为 False，以禁用主机名检查。然后，我们将 verify_mode 属性设置为 ssl.CERT_NONE，以取消校验
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        self.host = host
        self.cookie = None
        self.conn = http.client.HTTPSConnection(self.host, context=context)
        # self.conn = http.client.HTTPSConnection(self.host)

    def send_get_request(self, path):
        """Get 请求"""
        method_name = inspect.currentframe().f_code.co_name
        self.conn.request("GET", path)
        response_data = self.conn.getresponse().read().decode()
        self.conn.close()
        return response_data, method_name

    def send_post_request(self, path, body, headers=None):
        """POST 请求"""
        print(path, body)
        method_name = inspect.currentframe().f_code.co_name
        # 根据请求头判断数据类型
        content_type = headers.get("Content-Type", "").lower()
        if content_type == "application/json":
            # body = json.dumps(body)
            body = body.encode('utf-8')
        elif content_type == "application/x-www-form-urlencoded":
            body = urlencode(body).encode('utf-8')
        else:
            raise ValueError("Unsupported Content-Type in headers.")
        self.conn.request("POST", path, body, headers)
        response_data = self.conn.getresponse().read()
        self.conn.close()
        return response_data, method_name

    @method_decorator
    def send_put_request(self, path, body, headers=None):
        """PUT 请求"""
        method_name = inspect.currentframe().f_code.co_name
        # 根据请求头判断数据类型
        content_type = headers.get("Content-Type", "").lower()
        if content_type == "application/json":
            # body = json.dumps(body)
            body = body.encode('utf-8')
        elif content_type == "application/x-www-form-urlencoded":
            body = urlencode(body)
        else:
            raise ValueError("Unsupported Content-Type in headers.")
        self.conn.request("PUT", path, body, headers)
        response = self.conn.getresponse()
        response_data = response.read()
        self.conn.close()
        return response_data, method_name

    def send_delete_request(self, path):
        """DELETE 请求"""
        method_name = inspect.currentframe().f_code.co_name
        self.conn.request("DELETE", path)
        response = self.conn.getresponse()
        response_data = response.read()
        self.conn.close()
        return response_data, method_name

    def save_response_data(self, response_data, method_name, path=None):
        try:
            # 将响应数据解析为JSON
            json_data = json.loads(response_data)
            # 将JSON数据写入文件
            path = "/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/gitee/api_v1测试数据/"
            with open(path + "{}_response.json".format(method_name), "w") as file:
                json.dump(json_data, file, indent=4)
            print("{} 已写入文件：{}_response.json".format(method_name, method_name))
        except json.JSONDecodeError:
            # with open(path + "{}_response.txt".format(method_name), "w") as file:
            #     file.write(response_data.decode())
            print("响应无法解析为JSON，{} 已写入文件：{}_response.txt".format(method_name, method_name))


if __name__ == '__main__':
    """
    注意：POST 和 PUT 请求
    1、请求体是 json，json 格式需要加 ''' '''，方法里注释 # body = json.dumps(body)
    2、请求体是 form，注释 json 和 dict 转换的代码
    """

    # CI 环境
    # client = HttpClient("www.demo.com")

    time = datetime.now().strftime("%Y%m%d%H%M%S")

    # 发送 GET 请求
    # 获取 README
    # path = "/path/wei-demo-012/readme?access_token=15519cacadfc79c03a56f63892ca6840"
    # 获取 blob
    # path = "/path/wei-demo-012/blob/testfile/test_20230922143823.txt?access_token=15519cacadfc79c03a56f63892ca6840"
    # 获取 tree
    # path = "/path/wei-demo-016/tree?access_token=15519cacadfc79c03a56f63892ca6840"
    # response_data, method_name = client.send_get_request(path)
    # client.save_response_data(response_data, method_name)
    # print(response_data)

    # 发送 POST 请求
    # path = "/path/wei-demo-012/blob/testfile/test_{}.txt".format(time)
    body = '''{
        "access_token": "15519cacadfc79c03a56f63892ca6840",
        "owner": "testent001",
        "repo": "wei-demo-012",
        "content": "api 测试",
        "encoding": "text",
        "message": "api 创建",
        "author[name]": "git123",
        "author[eamil]": "git123@qq.com"
    }'''

    data_dict = json.loads(body)
    # data_dict["message"] = "api 创建 {}".format(time)
    # body = json.dumps(data_dict, indent=4)

    headers = {"Content-Type": "application/json"}
    # headers = {"Content-Type": "application/x-www-form-urlencoded"}
    # response_data, method_name = client.send_post_request(path, body, headers)
    # client.save_response_data(response_data, method_name)
    # print(response_data)

    # 发送 PUT 请求
    path = "/path/wei-demo-012/blob/testfile/test_20230922151044.txt"
    body = {
        "access_token": "15519cacadfc79c03a56f63892ca6840",
        "content": "更新 blob",
        "encoding": "text",
        "message": "更新 blog",
        "branch": "master"
    }

    # data_dict = json.loads(body)
    # data_dict["message"] = "更新 blog {}".format(time)
    # body = json.dumps(data_dict, indent=4)

    # headers = {"Content-Type": "application/json"}
    # headers = {"Content-Type": "application/x-www-form-urlencoded"}
    # response_data, method_name = client.send_put_request(path, body, headers)
    # client.save_response_data(response_data, method_name)
    # print(response_data)

    # 发送 DELETE 请求
    path = "api/v1/repos/testent001/wei-demo-012/blob/tmp.txt?access_token=15519cacadfc79c03a56f63892ca6840&message=%E5%88%A0%E9%99%A4blob"
    # response_data, method_name = client.send_delete_request(path)
    # client.save_response_data(response_data, method_name)
    # print(response_data)
    
