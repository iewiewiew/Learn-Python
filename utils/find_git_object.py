# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/16 10:09
@description  .git/objects 注：未实践成功
"""

import hashlib
import zlib


def object_path(content):
    header = f"blob {len(content)}\0"
    data = header.encode() + content
    sha1 = hashlib.sha1()
    sha1.update(data)
    digest = sha1.hexdigest()
    return f".git/objects/{digest[:2]}/{digest[2:]}"


def decompress_demo(path):
    with open(path, "rb", encoding='utf-8') as f:
        content = f.read()
        print(zlib.decompress(content).decode())


if __name__ == '__main__':
    """
    file .git/objects/58/80a3ea46355a6594a793942e832ae3f7661284
    """

    path = "/Users/menghuawei/PycharmProjects/Learn-Python/.git/objects/58/80a3ea46355a6594a793942e832ae3f7661284"

    decompress_demo(path)

    print(object_path(path))



