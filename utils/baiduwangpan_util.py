# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/9/22 10:00
@description  百度网盘 注：未实践成功
"""

"""
安装：pip install bypy，然后输入 bypy list，复制链接到浏览器打开，复制授权码到终端，按回车键即可完成安装，此时百度网盘我的应用数据下会出现一个 bypy 目录。
"""


def demo():
    from bypy import ByPy
    bp = ByPy()
    # 查看bypy的子目录及文件
    ld = bp.list()

    # 查看指定目录的子目录及文件
    ld_1 = bp.list('tmp.md')
    print(ld, ld_1)
    
    # 下载目录到本地。'tmp.md'指百度云盘我的应用数据目录中bypy目录下目录名。
    # bp.download('tmp.md', '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/tmp.md')
    
    # 下载文件到本地。注意只能用"/",不能用"\\"。
    # bp.download('tmp.md/0.docx', '/Users/menghuawei/PycharmProjects/Learn-Python/.tmp')
    
    # 上传文件到bypy。
    bp.upload('/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/tmp.md')
   
    # 上传文件到网盘指定目录。
    # bp.upload('/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/tmp.md', 'tmp.md')
    
    # 上传目录到网盘指定目录。python接单为bypy下的目录。
    # bp.upload('/Users/menghuawei/PycharmProjects/Learn-Python/.tmp/tmp.md', 'tmp.md')
