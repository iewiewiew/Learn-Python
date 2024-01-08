# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/22 13:58
@description  数据库 注：未实践成功

python -m pip install flask==1.1.2
python -m pip install flask_migrate==2.7.0
python -m pip install flask_sqlalchemy
python -m pip install flask_script
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand
from flask_migrate import Migrate
from flask_script import Manager, Server

# 实例化一个Flask 对象
app = Flask(__name__)

# 设置连接数据库的配置,这是以mysql db 为示例来讲解
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/dbname"

# 如果设置为True,将跟踪对象的修改并发出信号，默认设置为None
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 这个对象就包含 sqlalchemy 和 sqlalchemy.orm 中的所有函数和助手
db = SQLAlchemy(app)

manager = Manager(app)
Migrate(app, db)
# 创建数据库映射命令
manager.add_command('db', MigrateCommand)

# 创建启动命令
manager.add_command('start', Server(port=8000, use_debugger=True))


class Role(db.Model):  # 提供一个名为 Model 的类，用于作为声明模型时的 delarative 基类
    __tablename__ = 'roles'  # 给表起名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    us = db.relationship("User", backref="role")
    icon = db.Column(db.String(40), default='default.jpg')

    def __repr__(self):  # 用于显示一个可读字符串
        return "Role:%s" % self.name


class User(db.Model):
    __tablename__ = 'users'  # 给表起名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return "User:%s" % self.name


if __name__ == '__main__':
    # db.drop_all() # db 对象调用 SQLAlchemy.drop_all() 方法来删除表:
    # db.create_all() # db 对象调用 SQLAlchemy.create_all() 方法来创建表:
    # manager.run()

    # 创建
    role1 = Role(name="admin")
    role2 = Role(name="test")
    db.session.add(role1)
    db.session.commit()
    db.session.add(role2)
    db.session.commit()  # 必须提交会话，但是没有必要在每个请求后删除它(session)，Flask-SQLAlchemy 会帮您完成删除操作

    user1 = User(name="wang", email="test1@126.com", pswd="1234", role_id=role1.id)
    user2 = User(name="test", email="test2@126.com", pswd="1234", role_id=role2.id)
    db.session.add_all([user1, user2])
    db.session.commit()

    # 查询
    user1 = User.query.filter_by(name="wang")
    roles = Role.query.all()
    for role in roles:
        print(role.name, role.id)

    # 删除
    user = User.query.first()
    db.session.delete(user)
    db.session.commit()
    print(User.query.all())
    print("*")
    print(user)

    # 更新
    user = User.query.first()
    user.name = "test"
    db.session.commit()
    print(User.query.first())
