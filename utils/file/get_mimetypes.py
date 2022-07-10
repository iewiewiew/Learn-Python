# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/26 16:17
@description  查看MIME类型

MIME（Multipurpose Internet Mail Extensions）类型是一种标准，用于表示在Internet上交换的多媒体文件的类型。MIME类型通常由两部分组成，用斜杠分隔：主类型和子类型。例如，text/html是一种MIME类型，其中主类型为"text"，子类型为"html"。
在Web开发中，MIME类型通常与HTTP协议一起使用，以便浏览器可以正确地处理服务器发送的响应。例如，当服务器向浏览器发送HTML文件时，它会附加一个Content-Type头，指定文件的MIME类型。浏览器根据这个MIME类型来判断如何显示该文件，例如将其解析为HTML代码并在屏幕上呈现出来。
除了标准的MIME类型，还有一些自定义或非标准的MIME类型。这些类型通常以"x-"开头，并可能只在特定应用程序或环境中使用。例如，自定义MIME类型application/x-tar用于表示tar归档文件的内容。
总之，MIME类型是一种用于描述互联网上不同类型文件的标准，可以帮助确保不同的应用程序可以正确地处理和显示这些文件

常用的MIME类型及其相关信息：
text/html：HTML文档
application/json：JSON数据
image/jpeg：JPEG图像
image/png：PNG图像
application/pdf：PDF文件
application/zip：ZIP归档文件
audio/mpeg：MP3音频文件
video/mp4：MP4视频文件
application/msword：Word文档
application/vnd.ms-excel：Excel电子表格
application/xml：XML数据
text/plain：纯文本文件
"""

import mimetypes
import os


def demo1():
    # 指定文件路径
    file_path = '/docs/requirements.txt'

    # 使用文件扩展名猜测MIME类型
    mime_type = mimetypes.guess_type(file_path, strict=False)[0]
    print(mime_type)


def demo2():
    file_path = '../../file'
    for root, dirs, files in os.walk(file_path):
        for _file_path in files:
            path = os.path.join(root, _file_path)
            mime_type = mimetypes.guess_type(path, strict=False)[0]
            print("文件名称: %s        MIME类型: %s" % (_file_path, mime_type))
            print(1)


if __name__ == '__main__':
    # demo1()
    demo2()
