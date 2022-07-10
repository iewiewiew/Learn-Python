#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author        weimenghua
@time          2022/4/1 8:18
@description   re模块：正则表达式
"""

import re


def re_demo():
    print("search ", re.search(r'abc', 'abcef'))
    print("fullmatch ", re.fullmatch(r'abc', 'abcef'))
    print("fullmatch ", re.fullmatch(r'abc', 'abc'))

    """
    元字符   匹配内容
    .	匹配除换行符以外的任意字符
    \w	匹配字母或数字或下划线
    \s	匹配任意的空白符
    \d	匹配数字
    \n	匹配一个换行符
    \t	匹配一个制表符
    \b	匹配一个单词的结尾
    ^	匹配字符串的开始
    $	匹配字符串的结尾
    \W	匹配非字母或数字或下划线
    
    re.sub共有五个参数：
    其中三个必选参数：pattern, repl, string
    两个可选参数：count, flags
    其中r'\w+'为正则表达式，匹配多个英文单词或者数字，'12'为被替换的内容，“abc 23 de 5f, gh”是re匹配的字符串内容，count只替换前2个，flag表示忽略大小写
    """
    str = re.sub(r'\w+', '12', "abc 23 de 5f, gh", 2, flags=re.I)
    print(str)


if __name__ == '__main__':
    re_demo()
