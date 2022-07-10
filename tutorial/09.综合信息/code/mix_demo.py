# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/11 16:51
@description  不知道咋归类

在这段代码中，TestMetrics 是一个类，它接受关键字参数。run_case_data 是一个字典，包含了作为关键字参数的键值对。
**run_case_data 是一种将字典解包为关键字参数的方式。它将字典中的键值对作为关键字参数传递给 TestMetrics 类的构造函数。
return TestMetrics(**run_case_data) 表示将解包后的关键字参数传递给 TestMetrics 类的构造函数，并创建一个 TestMetrics 类的实例。然后，该实例被作为返回值返回。
换句话说，这行代码的作用是使用 run_case_data 字典中的键值对创建一个 TestMetrics 类的实例，并将该实例作为函数的返回值。通过使用 ** 运算符进行解包，可以将字典中的键值对转换为关键字参数，传递给类的构造函数。这种方式可以方便地将字典中的数据传递给接受关键字参数的函数或类的构造函数。
"""


class TestMetrics:
    def __init__(self, passed, failed, broken, skipped, total):
        self.passed = passed
        self.failed = failed
        self.broken = broken
        self.skipped = skipped
        self.total = total


run_case_data = {
    "passed": 10,
    "failed": 3,
    "broken": 2,
    "skipped": 5,
    "total": 20
}


def get_test_metrics(data):
    return TestMetrics(**data)


metrics = get_test_metrics(run_case_data)

print(metrics.passed)  # Output: 10
print(metrics.failed)  # Output: 3
print(metrics.broken)  # Output: 2
print(metrics.skipped)  # Output: 5
print(metrics.total)  # Output: 20
