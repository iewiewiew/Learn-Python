# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/12/2 08:30
@description  文件分类
"""

import os
import shutil


def get_file_type(file_path):
    # 获取文件扩展名
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()


def organize_files(input_folder):
    # 获取输入文件夹中的所有文件
    files = os.listdir(input_folder)

    # 遍历每个文件
    for file in files:
        # 构建文件的完整路径
        file_path = os.path.join(input_folder, file)

        # 判断是否是文件
        if os.path.isfile(file_path):
            # 获取文件类型
            file_type = get_file_type(file_path)

            # 构建目标文件夹路径
            target_folder = os.path.join(input_folder, file_type + '类')

            # 如果目标文件夹不存在，创建它
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # 构建目标文件路径
            target_file_path = os.path.join(target_folder, file)

            # 移动文件到目标文件夹
            shutil.move(file_path, target_file_path)


if __name__ == '__main__':
    organize_files('/Users/menghuawei/PycharmProjects/Learn-Python/file/tmp')
