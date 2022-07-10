#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      weimenghua
@time        2021/10/29 18:35
@description pymysql模块：连接数据库
import pymysql，此模块是默认开启mysql的事务功能的，因此，进行“增”、“删”、“改”的时候，一定要使用db.commit()提交事务，否则就看不见所插入的数据。
"""
import random
import pymysql


def conn_database():
    """连接数据库"""
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='dbname',
                              charset='utf8')
    cursor = connect.cursor()
    if connect:
        print("连接数据库成功！")
    sql = "select * from dbname.`t_table_info`"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        for row in result:
            id = row[0]
            name = row[1]
            age = row[2]
            sex = row[3]
            print("id=%s name=%s age=%s sex=%s" % (id, name, age, sex))
    except:
        print("出错啦")


def show_dbs():
    """查询数据库"""
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='dbname',
                              charset='utf8')
    cursor = connect.cursor()

    query1 = 'SHOW DATABASES'
    cursor.execute(query1)
    result = cursor.fetchall()
    for row in result:
        print('所有数据库: ', row[0])

    query2 = 'SHOW TABLES'
    cursor.execute(query2)
    result = cursor.fetchall()
    for row in result:
        print('所有数据表: ', row[0])


def create_table():
    """创建表"""
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='dbname', charset='utf8')
    cursor = db.cursor()
    # 检查表是否存在，如果存在删除
    sql1 = 'drop table if exists students'
    cursor.execute(sql1)
    sql2 = 'create table students(id int auto_increment primary key not null,name varchar(10) not null,age int not null)'
    cursor.execute(sql2)
    print("创建成功")
    db.close()


def insert_table():
    """插入数据"""
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='dbname', charset='utf8')
    cursor = db.cursor()
    sql = 'insert into students(name,age) values(%s,%s)'
    try:
        cursor.execute(sql, ('孙悟空', 1010))
        print("插入成功")
        db.commit()
    except:
        print("插入失败")
        db.rollback()
    db.close()


def update_table():
    """更新数据"""
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='dbname', charset='utf8')
    cursor = db.cursor()
    sql = 'update students set age =%s where name=%s'
    try:
        cursor.execute(sql, (30, "孙悟空"))
        print("更新成功")
        db.commit()
    except:
        print("更新失败")
        db.rollback()
    db.close()


def delete_table():
    """删除数据"""
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='dbname', charset='utf8')
    cursor = db.cursor()
    sql = 'delete from dbname.`students` where id=2;'
    try:
        cursor.execute(sql)
        print("删除成功？")
        db.commit()
    except:
        print("删除失败")
        db.rollback()
    db.close()


def fetch_table():
    """查询数据"""
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', database='dbname', charset='utf8')
    cursor = db.cursor()
    sql = 'select * from dbname.`students`;'
    try:
        cursor.execute(sql)
        reslist = cursor.fetchall()
        for row in reslist:
            print("%s %s %s" % (row[0], row[1], row[2]))
    except:
        print("查询失败")
        db.rollback()
    db.close()


def delete_database():
    """删除数据库"""
    # 创建MySQL连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', charset='utf8')

    # 获取MySQL连接的游标
    cursor = db.cursor()

    # 删除数据库
    list = ['iotdb', 'liuma', 'springboot-vue']
    for i in list:
        print('DROP DATABASE IF EXISTS {}'.format(i))
        cursor.execute('DROP DATABASE IF EXISTS {}'.format(i))

    # 提交更改
    db.commit()

    # 关闭游标和链接
    cursor.close()
    db.close()


if __name__ == '__main__':
    show_dbs()
    # create_table()
    # insert_table()
    # update_table()
    # delete_table()
    # fetch_table()
    # delete_database()
