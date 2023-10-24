# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/12/5 14:31
@description  调用模型引擎接口
"""

import requests

API_URL = "https://ai.gitee.com/api/endpoints/iewiewiew/gpt2-6602/inference"
headers = {
    "Authorization": "Bearer eyJpc3MiOiJodHRwczovL2FpLmdpdGVlLmNvbSIsInN1YiI6IjIxIn0.llnKA64EXIYIHQZRykJjd9GuXxvhhLP9tqJxvfNPT6szPhVHlV-7_7dgdQKaLsLd79C1ilrKLhEq6g-TA6I1CQ",
    "Content-Type": "application/json"
}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


if __name__ == '__main__':
    output = query({
        "inputs": "Can you please let us know more details about your ",
    })
    print(output)
