# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/4/16 1:02
@description  数据库表模型
python manage.py migrate   # 创建表结构
python manage.py makemigrations apps  # 让Django知道我们在我们的模型有一些变更
python manage.py migrate apps   # 创建表结构
"""

from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    title = models.CharField(max_length=32)  # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 书籍价格
    publish = models.CharField(max_length=32)  # 出版社名称
    pub_date = models.DateField()  # 出版时间
