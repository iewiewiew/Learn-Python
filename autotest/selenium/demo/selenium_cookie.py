# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/21 22:26
@description  cookie操作

1、get_cookies() 获得所有 cookie 信息
2、get_cookie(name) 返回有特定 name 值有 cookie 信息
3、add_cookie(cookie_dict) 添加 cookie，必须有 name 和 value 值
4、delete_cookie(name) 删除特定(部分)的 cookie 信息
5、delete_all_cookies() 删除所有 cookie 信息
"""

from selenium import webdriver
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(1)

    print(driver.get_cookies())

    # 向 cookie 的 name 和 value 添加会话信息。
    driver.add_cookie({'name': 'key-a', 'value': 'value-a'})

    # 遍历 cookies 中的 name 和 value 信息打印，当然还有上面添加的信息
    for cookie in driver.get_cookies():
        print("%s -> %s" % (cookie['name'], cookie['value']))

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
