# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/8/18 15:56
@description  生成随机中文
"""

import random


def generate_chinese_characters(num):
    characters = []
    for _ in range(num):
        # 生成一个随机的中文字符的Unicode码
        # char_code = random.randint(0x4e00, 0x9fbf)
        char_code = random.randint(0x4e00, 0x9fbf)
        # 将Unicode码转换为字符并添加到列表中
        characters.append(chr(char_code))
    # return characters
    return ''.join(characters)


if __name__ == '__main__':
    # 生成10个中文字符
    chinese_characters = generate_chinese_characters(10)
    print(chinese_characters)
