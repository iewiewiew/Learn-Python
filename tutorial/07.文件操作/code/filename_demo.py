# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/24 16:26
@description
"""
import os


# xx_yy_zz --> XxYyZz
import yaml


def capitalize_demo():
    file_name = "/aa/bb/cc/xx_yy_zz.py"
    file_name = os.path.split(file_name)[1][:-3]
    name = file_name.split("_")
    name_len = len(name)
    for i in range(name_len):
        name[i] = name[i].capitalize()
    class_name = "".join(name)
    print(class_name)


# xx_yy_zz.py --> test_xx_yy_zz.py
def split_path():
    file_name = "/aa/bb/cc/xx_yy_zz.py"
    path = file_name.split(os.sep)
    path[-1] = path[-1].replace(path[-1], "test_" + path[-1])
    print(path, path[-1])


def get_all_files(file_path, yaml_data_switch=False) -> list:
    """
    获取文件路径
    :param file_path: 目录路径
    :param yaml_data_switch: 是否过滤文件为 yaml 格式，True 则过滤
    """
    filename = []
    # 获取所有文件下的子文件名称
    for root, dirs, files in os.walk(file_path):
        print(root, dirs, files)
        for _file_path in files:
            path = os.path.join(root, _file_path)
            if yaml_data_switch:
                if 'yaml' in path or '.yml' in path:
                    filename.append(path)
            else:
                filename.append(path)
    return filename


def yaml_demo():
    data = {
        'name': 'John Smith',
        'age': 20,
        'interests': [
            'Reading',
            'Sports'
        ]
    }

    with open('../../../file/data.yaml', 'w') as f:
        yaml.dump(data, f)


if __name__ == '__main__':
    # file_path = "/autotest/autotestdemo/data"
    # print(get_all_files(file_path))
    yaml_demo()