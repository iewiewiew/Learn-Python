# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/14 16:35
@description  创建大文件
"""


def create_large_binary_file(file_path, file_size):
    with open(file_path, 'wb') as file:
        chunk_size = 1024  # 每次写入的块大小
        bytes_written = 0  # 已写入的字节数

        while bytes_written < file_size:
            remaining_bytes = file_size - bytes_written
            write_size = min(chunk_size, remaining_bytes)
            chunk = b'\x00' * write_size  # 用于写入的数据块，这里使用空字节（0x00）

            file.write(chunk)
            bytes_written += write_size


if __name__ == '__main__':
    file_path = '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/large_file.bin'
    file_size = 1024 * 1024 * 100  # 文件大小为 100 MB
    create_large_binary_file(file_path, file_size)
