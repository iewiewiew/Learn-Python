# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/4 12:21
@description  定义一个 Student 类
"""


class Student(object):
    """
    __init__ 是一个特殊方法用于在创建对象时进行初始化操作, 通过这个方法为学生对象绑定 name 和 age 两个属性。其参数通常以self开头，表示对当前对象的引用。
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s 正在学习%s' % (self.name, course_name))

    def play(self):
        if self.age > 18:
            print('%s 可以坐过山车' % (self.name))
        else:
            print('%s 可以坐选择木马' % (self.name))


if __name__ == '__main__':
    stu = Student('不洗碗', 20)
    stu.study("Python")
    stu.play()
