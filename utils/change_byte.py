# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/3/11 17:17
@description  把 Byte 转换为其它单位
"""


def convert_bytes(byte_value, decimal_places=2):
    """
    将字节数转换为其他单位大小
    :param byte_value: 字节数
    :param decimal_places: 小数点后保留的位数，默认为 2
    :return: 转换后的值和单位的字符串列表
    """
    if byte_value < 0:
        raise ValueError("字节数不能为负数")

    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    converted_values = []

    for unit in units:
        converted_value = byte_value / (1024 ** units.index(unit))
        converted_values.append(f"{converted_value:.{decimal_places}f} {unit}")

    return converted_values


if __name__ == '__main__':
    byte_value = 2170732
    converted_values = convert_bytes(byte_value)
    print(converted_values)
