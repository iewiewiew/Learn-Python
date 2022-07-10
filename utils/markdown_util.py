# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/14 13:44
@description  给markdown目录生成序号
"""


import re


def replace_title_num(markdown_src, markdown_dst):
    """
    替换标题序号
    :param markdown_src: markdown源文件
    :param markdown_dst: markdown目标文件
    :return:
    """
    with open(markdown_src, 'rb') as f:
        txt = f.read().decode()

    # 默认6个标题等级
    heading_level = [0] * 7

    # 正则表达式编译标题格式，必须是 1-6个#和空格开始
    head_pattern = re.compile("^(#{1,6}) ")
    new_markdown = []

    for line in txt.splitlines():
        result = re.search(head_pattern, line)
        if not result:
            new_markdown.append(line)
            continue

        level = len(result.group(1))
        heading_level[level] += 1

        # int 转 str
        num_str = map(str, heading_level[1:level+1])
        # 拼接并替换字符串
        title = f"{result.group(1)} {'.'.join(num_str)}."
        heading_level[level+1:] = [0]*(7-level)

        line = line.replace(result.group(1), title)
        new_markdown.append(line)

    new_content = "\n".join(new_markdown)

    with open(markdown_dst, "w", encoding='utf8') as f:
        f.write(new_content)


def replace_title_num(markdown_src, markdown_dst):
    """
    替换标题序号
    :param markdown_src: markdown源文件
    :param markdown_dst: markdown目标文件
    :return:
    """
    with open(markdown_src, 'rb') as f:
        txt = f.read().decode()

    # 默认6个标题等级
    heading_level = [0] * 7

    # 正则表达式编译标题格式，必须是 1-6个#和空格开始
    head_pattern = re.compile("^(#{1,6}) ")
    new_markdown = []

    for line in txt.splitlines():
        result = re.search(head_pattern, line)
        if not result:
            new_markdown.append(line)
            continue

        level = len(result.group(1))
        heading_level[level] += 1

        # int 转 str
        num_str = map(str, heading_level[1:level+1])
        # 拼接并替换字符串
        title = f"{result.group(1)} {'.'.join(num_str)}."
        heading_level[level+1:] = [0]*(7-level)

        line = line.replace(result.group(1), title)
        new_markdown.append(line)

    new_content = "\n".join(new_markdown)

    with open(markdown_dst, "w", encoding='utf8') as f:
        f.write(new_content)


if __name__ == '__main__':
    # markdown_src = r"/Users/menghuawei/IdeaProjects/my-project/wei-notebook/Linux/Linux 命令.md"
    # markdown_dst = r"/Users/menghuawei/IdeaProjects/my-project/wei-notebook/Linux/Linux 命令(序号目录).md"

    markdown_src = r"/Users/menghuawei/IdeaProjects/my-project/wei-notebook/Mixinfo/Markdown/Markdown教程.md"
    markdown_dst = r"/Users/menghuawei/IdeaProjects/my-project/wei-notebook/Mixinfo/Markdown/Markdown教程(序号目录).md"
    replace_title_num(markdown_src, markdown_dst)

    # markdown_src = r"../autotest/pytest/Pytest 自动化测试框架.md"
    # markdown_dst = r"../autotest/pytest/pytest手册(序号目录).md"
    # replace_title_num(markdown_src, markdown_dst)