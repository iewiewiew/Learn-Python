# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/11 08:31
@description  SQLAlchemy是一个Python SQL工具包和对象关系映射器，用于简化数据库操作

pip install sqlalchemy
pip install mysql-connector-python
"""

import sqlalchemy
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

# @todo 未实践成功

# 创建对象的基类:
Base = sqlalchemy.orm.declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user001'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


if __name__ == '__main__':
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/dbname')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
