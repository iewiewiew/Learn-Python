# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author      weimenghua
@time        2020/7/11 21:11
@description str 字符串
"""


def demo():
    str = 'abcdefg'
    print("第一个值 " + str[0])
    print("第二个值 " + str[1])
    print("取下标为2~3的字符 " + str[2:4])
    print("取下标为2开始到最后的字符 " + str[2:])


mystr = 'hello world itcast and itcastcpp'


def demo1():
    # 1、find，检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
    # mystr.find(str, start=0, end=len(mystr))
    mystr.find('hello')
    print(mystr.find('hello'))  # 返回0
    print(mystr.find('xx'))  # 返回-1


def demo2():
    # 2、index，跟find()方法一样，只不过如果str不在mystr中会报一个异常.
    # mystr.index(str, start=0, end=len(mystr))
    mystr.index('hello')
    print(mystr.index('hello'))  # 返回0
    # print(mystr.index('xx')) #报错


def demo3():
    # 3、count，返回str在start和end之间在mystr里面出现的次数
    # mystr.count(str, start=0, end=len(mystr))
    mystr.count('hello')
    print(mystr.count('hello'))


def demo4():
    # 4、replace，把mystr中的str1替换成str2,如果count指定，则替换不超过count次
    mystr.replace('hello', 'hello2', mystr.count('hello'))
    print(mystr)


def demo5():
    # 5、split，以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
    mystr.split(',')
    print(mystr)


# 字符串转换
def change_str():
    str = "www.demo.com"
    print(str.upper())  # 把所有字符中的小写字母转换成大写字母
    print(str.lower())  # 把所有字符中的大写字母转换成小写字母
    print(str.capitalize())  # 把第一个字母转化为大写字母，其余小写
    print(str.title())  # 把每个单词的第一个字母转化为大写，其余小写


if __name__ == '__main__':
    demo()
    demo1()
    demo2()
    demo3()
    demo4()
    demo5()
    change_str()
