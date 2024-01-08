# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/26 10:45
@description  实时监控指定文件夹的变化（如文件添加、删除、修改）
"""

import time
import os


def monitor_folder_changes(folder_path):
    initial_files = set(os.listdir(folder_path))
    while True:
        current_files = set(os.listdir(folder_path))
        new_files = current_files - initial_files
        deleted_files = initial_files - current_files
        if new_files:
            print(f"Added: {new_files}")
        if deleted_files:
            print(f"Deleted: {deleted_files}")
        initial_files = current_files
        time.sleep(1)


if __name__ == '__main__':
    monitor_folder_changes('/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/tmp')
