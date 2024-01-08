# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/8 16:34
@description
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description='计算两个数的乘积')
    parser.add_argument('num1', type=float, help='第一个数')
    parser.add_argument('num2', type=float, help='第二个数')
    args = parser.parse_args()

    result = args.num1 * args.num2
    print(f'乘积：{result}')


def main2():
    parser = argparse.ArgumentParser(description='选择模板')
    parser.add_argument('-t', '--template', help='指定模板路径')
    args = parser.parse_args()

    if args.template:
        print(f'使用模板：{args.template}')
    else:
        print('没有指定模板参数。')


if __name__ == '__main__':
    main()
    """
    python argparse_example.py 2 3
    """
