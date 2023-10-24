# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/8/1 08:57
@description  unicode/base64/urllib
"""

import json
import base64


def unicode_demo():
    """unicode 编码"""

    str1 = b"\u53ea\u5141\u8bb8\u5728\u5206\u652f\u4e0a\u521b\u5efa\u6216\u66f4\u65b0\u6587\u4ef6"
    print(str1.decode("unicode_escape"))  # 使用unicode_escape 解码

    str2 = r'\u4f60\u597d'
    print(str2.encode().decode("unicode_escape"))  # 使用encode()方法转换，再调用bytes.decode()转换为字符串形式

    str3 = '\u4f60\u597d'
    print(json.loads('"%s"' % str3))  # 使用json.loads 解码（为json 格式）


def base64_demo():
    """base64 编码"""

    # 文本字符串进行 Base64 编码
    text = "更新 blog 123"
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    encoded_text = encoded_bytes.decode("utf-8")
    print("Base64 编码后的字符串:", encoded_text)

    # Base64 编码的字符串进行解码
    decoded_bytes = base64.b64decode(encoded_text)
    decoded_text = decoded_bytes.decode("utf-8")
    print("Base64 解码后的字符串:", decoded_text)


def url_demo():
    """url 编码"""

    from urllib.parse import quote, quote_plus, unquote, unquote_plus

    # URL 编码
    url = "https://www.example.com/?name=John Doe"

    encoded_url = quote(url)
    print("Encoded URL:", encoded_url)

    # URL 解码
    decoded_url = unquote(encoded_url)
    print("Decoded URL:", decoded_url)

    # URL 编码，将空格转换为加号
    encoded_url_plus = quote_plus(url)
    print("Encoded URL (plus):", encoded_url_plus)

    # URL 解码，将加号转换为空格
    decoded_url_plus = unquote_plus(encoded_url_plus)
    print("Decoded URL (plus):", decoded_url_plus)


if __name__ == '__main__':
    # unicode_demo()
    base64_demo()
    # url_demo()
