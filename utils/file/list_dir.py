# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/11 08:22
@description  导出文件目录树状结构
"""

import os


def list_files_in_directory(path='.', include_subdirectories=False, indent_level=0):
    """
    列出指定目录下的文件和文件夹，并以树状图格式显示。

    :param path: 要列出文件的目录路径，默认为当前目录。
    :param include_subdirectories: 是否包括子目录中的文件，默认为 False。
    :param indent_level: 缩进级别，用于区分不同层级，默认为 0。
    """
    try:
        # 获取指定目录下的所有文件和文件夹
        items = os.listdir(path)

        # 遍历文件和文件夹
        for item in items:
            item_path = os.path.join(path, item)

            # 使用缩进来区分不同层级
            print("   " * indent_level, end="")

            # 判断是否为文件夹
            if os.path.isdir(item_path):
                print(f"└── {item}/")
                # 如果包括子目录并且当前项目是文件夹，则递归列出子目录下的文件
                if include_subdirectories:
                    list_files_in_directory(item_path, include_subdirectories, indent_level + 1)
            else:
                print(f"├── {item}")

    except Exception as e:
        print(f"发生错误：{str(e)}")


if __name__ == "__main__":
    # 调用函数并传递参数以满足您的需求
    list_files_in_directory(path='.', include_subdirectories=True)
