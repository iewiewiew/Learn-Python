# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/15 18:39
@description  创建多种文件
"""

import os

# 要创建的文件类型列表
file_types = ['.txt', '.md', '.xlsx', '.docx', '.csv', '.json']

# 要创建的文件数量
num_files = 2

# 要创建文件的根目录
root_directory = '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/file'

# 循环创建文件
for i in range(num_files):
    for file_type in file_types:
        # 获取文件的扩展名（后缀名）
        file_extension = os.path.splitext(file_type)[1]

        # 构建子目录路径
        subdirectory = file_extension.strip('.')
        directory_path = os.path.join(root_directory, subdirectory)

        # 如果子目录不存在，则创建子目录
        os.makedirs(directory_path, exist_ok=True)

        # 构建文件路径
        file_name = f"file_{i+1}{file_type}"
        file_path = os.path.join(directory_path, file_name)

        # 创建并写入文件
        with open(file_path, 'w') as file:
            file.write(f"This is {file_name}.")

        print(f"Created file: {file_path}")