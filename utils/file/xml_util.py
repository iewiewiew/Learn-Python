# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/11 14:07
@description  xml 相关操作
"""

import xml.etree.ElementTree as ET

tree = ET.parse('../../file/xml_demo.xml')
root = tree.getroot()

# 遍历XML文档
for element in root.iter():
    print(element.tag, element.text)
