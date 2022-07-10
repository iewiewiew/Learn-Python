# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/16 13:39
@description  飞书通知
"""

import requests


def send_feishu_notification(message, webhook_url):
    # 构建通知消息的数据
    payload = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }

    # 发送POST请求到飞书的Webhook地址
    response = requests.post(webhook_url, json=payload)

    # 检查请求的返回状态码
    if response.status_code == 200:
        print("飞书通知发送成功！")
    else:
        print("飞书通知发送失败！错误码：", response.status_code)


if __name__ == '__main__':
    # 设置飞书的Webhook地址
    webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/123456"

    # 调用函数发送飞书通知
    send_feishu_notification("这是一条来自Python的飞书通知！", webhook_url)
