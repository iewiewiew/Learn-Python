# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/6/4 12:47
@description  @property 装饰器：使用@property 包装器来包装 getter（访问器）和 setter（修改器）方法，使得对属性的访问既安全又方便
"""


class Student(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter 方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter 方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter 方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s 可以坐过山车' % self._name)
        else:
            print('%s 可以坐旋转木马' % self._name)


if __name__ == '__main__':
    stu = Student('不洗碗', 20)
    stu.play()
    stu.age = 12
    stu.play()
    # stu.name = '啦啦啦' # AttributeError: can't set attribute
