# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/24 09:00
@description  在目录中对文件进行排序
"""

import os
from shutil import move


def sort_files(directory_path):
    """Python脚本用于按文件扩展名对目录中的文件进行排序"""

    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_extension = filename.split('.')[-1]
            destination_directory = os.path.join(directory_path, file_extension)
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
                move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))


if __name__ == '__main__':
    directory_path = '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/tmp'
    sort_files(directory_path)
