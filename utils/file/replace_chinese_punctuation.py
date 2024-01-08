# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/2/27 11:32
@description  python 查找指定目录的指定后缀文件，把文件的所有中文标点符合改为英文标点符号
"""

import os
import re


def replace_chinese_punctuation(directory, file_extension):
    # 遍历指定目录及其子目录下的文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)

                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 使用正则表达式替换中文标点符号
                replaced_content = re.sub(r'[，。！？；：“”‘’【】（）]',
                                          lambda m: {
                                              '，': ',',
                                              '。': '.',
                                              '！': '!',
                                              '？': '?',
                                              '；': ';',
                                              '：“': ': "',
                                              '”': '"',
                                              '‘': "'",
                                              '’': "'",
                                              '【': '[',
                                              '】': ']',
                                              '（': '(',
                                              '）': ')'
                                          }.get(m.group(0), m.group(0)), content)

                # 将替换后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    print("替换文件: ", file_path)
                    f.write(replaced_content)


if __name__ == '__main__':
    # 指定目录和文件后缀
    directory = '/Users/menghuawei/IdeaProjects/my-project/Learn-Go/tutorial'  # 替换成你想要操作的目录路径
    file_extension = '.go'  # 替换成你想要处理的文件后缀

    replace_chinese_punctuation(directory, file_extension)
