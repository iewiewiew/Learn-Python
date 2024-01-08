# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/16 13:39
@description  飞书通知
"""
import base64
import json

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


def send_feishu_notification(webhook_url):
    headers = {
        "Content-Type": "application/json"
    }
    title = "飞书通知"
    content = "123"

    payload = {
        "title": title,
        "text": content,
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": title,
                    "content": [
                        [
                            {
                                "tag": "lark_md",
                                "text": "[开放平台](https://open.feishu.cn/)"
                            }
                        ]
                    ]
                }
            }
        }
    }
    response = requests.post(webhook_url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Notification sent successfully!", response.text)
    else:
        print("Failed to send notification. Error:", response.text)


def send_feishu_notification2(webhook_url):
    headers = {"Content-Type": "application/json"}
    data = {
      "msg_type": "post",
      "content": {
        "post": {
          "zh-CN": {
            "title": "标题",
            "content": [
              [
                {
                  "tag": "text",
                  "text": "请"
                },
                {
                  "tag": "a",
                  "text": "点击查看",
                  "href": "https://www.feishu.cn/hc/zh-CN/"
                },
                {
                  "tag": "a",
                  "text": "Markdown",
                  "href": "https://open.feishu.cn/document/common-capabilities/message-card/message-cards-content/using-markdown-tags"
                },
              ]
            ]
          }
        }
      }
    }

    response = requests.post(webhook_url, json=data, headers=headers)

    if response.status_code == 200:
        print("通知发送成功", response.json())
    else:
        print("通知发送失败")


def send_feishu_attachment(webhook_url):
    """
    飞书通知发送附件 未调通
    """

    # 附件的本地文件路径
    attachment_path = "/utils/file/email/statistics.xlsx"

    # 构建请求的 headers
    headers = {
        "Content-Type": "application/json"
    }

    # 读取附件文件的二进制数据
    with open(attachment_path, "rb") as file:
        attachment_data = file.read()

    # 使用 base64 编码将附件数据转换为文本字符串
    attachment_data2 = base64.b64encode(attachment_data).decode("utf-8")

    # 构建请求的 payload
    payload = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "附件示例",
                    "content": [
                        [
                            {
                                "tag": "text",
                                "text": "这是一条带附件的消息"
                            }
                        ]
                    ]
                }
            }
        },
        "attachments": [
            {
                "name": "statistics.xlsx",
                "content": attachment_data2
            }
        ]
    }

    # 发送请求
    response = requests.post(webhook_url, json=payload, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        print("附件发送成功")
    else:
        print("附件发送失败:", response.text)


if __name__ == '__main__':
    # 设置飞书的Webhook地址
    webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/123456"

    # 调用函数发送飞书通知
    # send_feishu_notification("这是一条来自Python的飞书通知！", webhook_url)
