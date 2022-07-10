# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/16 0:42
@description  Django的视图
"""

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello 学习Django项目")