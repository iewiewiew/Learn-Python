# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/10/11 15:14
@description  题目001: 在Python中如何实现单例模式。单例模式是指让一个类只能创建出唯一的实例。

单例模式适用于以下场景：
资源共享：当多个对象需要共享同一个资源时，可以使用单例模式确保只有一个实例管理该资源。例如，数据库连接池、线程池等。
配置信息：当需要全局访问和共享配置信息时，可以使用单例模式来管理配置对象，避免重复读取配置文件或多次创建配置对象。
日志记录：在日志记录的场景中，使用单例模式可以确保只有一个日志对象，实现统一的日志记录和管理。
缓存：当需要实现缓存功能时，可以使用单例模式来管理缓存对象，以便在多个地方共享和访问缓存数据。
控制资源实例数量：在某些情况下，系统需要限制某个类的实例数量，例如数据库连接池中的连接数。单例模式可以用于管理和控制实例数量。
"""

from functools import wraps


def singleton(cls):
    """单例类装饰器"""
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President:
    pass


if __name__ == '__main__':
    instances = President()
    print(instances)