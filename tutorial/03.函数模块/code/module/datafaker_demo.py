# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/3 10:07
@description  datafaker模块：生成大量测试数据

pip install datafaker
meta.txt文件中每行数据为元数据的一个字段描述，以||分割为三列，若以#开头，则忽略该行。
第一列：字段名
第二列：表字段类型
第三列：字段注释，其中包含构造规则标识
name不加标记则会随机产生20字符内的字符串，可以加上改为：学生名字[:name]
其中学校名字[:enum(file://./files/names.txt)]表示从本地文件names.txt中读取枚举数据，表示学校名称只能从下面这5所学校中随机产生。
"""

import os


def demo():
    os.system('datafaker rdb mysql+mysqldb://root:root@localhost:3306/dbname?charset=utf8 stu 10  --meta '
              '../files/meta.txt')


def demo1():
    os.system('datafaker rdb mysql+mysqldb://root:root@localhost:3306/dbname?charset=utf8 stu 10 --outprint --meta '
              'meta.txt --outspliter ,')


if __name__ == '__main__':
    demo()
