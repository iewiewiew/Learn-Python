# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/4 12:21
@description  私有属性和私有方法
"""


class Student(object):
    # 在属性前面加两个__表示属性私有
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    # 在方法前面加两个__表示方法私有
    def __study(self, course_name):
        print('%s 正在学习%s' % (self.__name, course_name))

    def __play(self):
        if self.age > 18:
            print('%s 可以坐过山车' % (self.__name))
        else:
            print('%s 可以坐旋转木马' % (self.__name))


if __name__ == '__main__':
    stu = Student('不洗碗', 20)

    stu._Student__study('Python')
    # stu.__study("python")  #直接访问私有方法会报错

    stu._Student__play()
