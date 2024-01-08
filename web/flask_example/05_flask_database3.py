# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/22 17:06
@description
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'UserInfo'
    index = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), unique=True)
    username = Column(String(30))
    passwd = Column(String(500))

    def __init__(self, index, user_id, username, passwd):
        self.index = index
        self.user_id = user_id
        self.username = username
        self.passwd = passwd


def mysql_db(host='127.0.0.1', dbname='dbname'):
    engine = create_engine("mysql+pymysql://root:root@{}:3306/{}?charset=utf8mb4".format(host, dbname))

    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return engine, session()


def add_data():
    # 新增数据
    engine, session = mysql_db()
    user = User(1, "11111", "zhangsan", "11111")
    session.add(user)
    session.commit()


def batch_add_data():
    # 批量新增数据
    engine, session = mysql_db()
    user1 = User("101", "lisi", "11111")
    user2 = User("102", "wangwu", "22222")
    session.add_all([user1, user2])
    session.commit()


def select_data():
    engine, session = mysql_db()
    users = session.query(User).filter_by(user_id=11111).all()

    for item in users:
        print(item.username, item.passwd)


def update_data():
    engine, session = mysql_db()
    session.query(User).filter_by(username="zhangsan").update({'passwd': "123456"})

    users = session.query(User).filter_by(username="zhangsan").first()
    users.username = "zhangsan-test"
    session.add(users)
    session.commit()


def delete_data():
    engine, session = mysql_db()
    session.query(User).filter(User.username == "zhangsan-test").delete()
    session.commit()


if __name__ == '__main__':
    # add_data()
    # batch_add_data()
    select_data()
    # update_data()
    # delete_data()
