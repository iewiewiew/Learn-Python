# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/8/8 12:28
@description  JSON Schema 模式是一个词汇表，可用于注释和验证 JSON 文档。
https://www.jsonschema.net/
"""

import requests
from jsonschema import validate


def demo():
    schema = {
        "type": "object",
        "properties": {
            "url": {
                "type": "string"
            },
            "origin": {
                "type": "string"
            }
        }
    }
    r = requests.post("https://httpbin.ceshiren.com/post")
    validate(instance=r.json(), schema=schema)


if __name__ == '__main__':
    demo()
