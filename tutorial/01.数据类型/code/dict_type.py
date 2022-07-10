#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@author      weimenghua
@time        2021/7/25 9:12
@description dict 字典
"""


def dict_demo():
    dict = {'name': 'zhangsan', 'age': 18, 'city': 'beijing'}
    print("输出dict: ", dict['name'])

    dict['age'] = 30
    print("修改dict：", dict['age'])

    dict['job'] = "coder"
    print("添加dict：", dict['job'])

    print("字典长度：", len(dict))

    print("输出字典：", str(dict))

    del dict['city']  # 删除键 'city'

    dict.clear()  # 清空字典

    del dict  # 删除字典


def dict_demo2():
    # 字典中的值又是一个字典(嵌套的字典)
    students = {
        1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
        1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
        1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
    }

    # 使用get方法通过键获取对应的值，如果取不到不会引发KeyError异常而是返回None或设定的默认值
    print(students.get(1002))  # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
    print(students.get(1005))  # None
    print(students.get(1005, {'name': '无名氏'}))  # {'name': '无名氏'}

    # 获取字典中所有的键
    print(students.keys())  # dict_keys([1001, 1002, 1003])
    # 获取字典中所有的值
    print(students.values())  # dict_values([{...}, {...}, {...}])
    # 获取字典中所有的键值对
    print(students.items())  # dict_items([(1001, {...}), (1002, {....}), (1003, {...})])
    # 对字典中所有的键值对进行循环遍历
    for key, value in students.items():
        print(key, '--->', value)


if __name__ == '__main__':
    # dict_demo()
    dict_demo2()
