# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/2/23 11:58
@description  数据类型

列表和元组的区别：
1、列表是动态数组，它们可变且可以重设长度（改变其内部元素的个数）。
2、元组是静态数组，它们不可变，且其内部数据一旦创建便无法改变。
3、元组缓存于Python运行时环境，这意味着我们每次使用元组时无须访问内核去分配内存。

这些区别结实率两者在设计哲学上的不同：
列表可被用于保存多个互相独立对象的数据集合。
元组用于描述一个不会改变的事务的多个属性。
"""


def data_type_demo():
    num = 123
    str = "张三"
    tup = ("张三", "李四", "王五")
    lis = ['a', 'b', 'c', 1, 2]
    dic = {'name': 'zhangsan', 'age': 18, 'city': 'beijing'}
    set = {'a', 'b', 'c', 'd', 'd'}
    print("数字：%d, 字符串：%s, 元组：%s, 列表：%s, 字典：%s, 集合：%s" % (num, str, tup, lis, dic, set))


# tuple不可变
def tuple_demo():
    demo = ("一", "二", "三")
    try:
        demo[0] = "四"
    except Exception as e:
        print("异常：" + repr(e))


# list可变
def list_demo():
    demo = ["一", "二", "三"]
    demo[0] = "四"
    print(demo[0])


if __name__ == '__main__':
    data_type_demo()
    tuple_demo()
    list_demo()
