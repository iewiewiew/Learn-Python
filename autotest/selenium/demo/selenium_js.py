# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/21 22:37
@description  js操作

1、滚动条是针对整个HTML：js = "var q=document.documentElement.scrollTop=10000"  # documentElement表示获取根节点元素
2、滚动条是针对整个body：js = "var q=document.body.scrollTop=10000"  # documentElement表示获取body节点元素
3、滚动条是针对某个div：js = "var q=document.getElementsByClassName('main')[0].scrollTop = 10000"  # getElementsByClassName表示获取class='main'的元素列表，0表示第一个，所以使用的时候要加索引
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(1)

    driver.find_element(By.ID, "kw").send_keys("selenium")
    driver.find_element(By.ID, "su").click()
    time.sleep(3)

    # 将页面滚动条拖到底部, 10000是最底部
    js1 = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js1)
    time.sleep(3)

    # 将滚动条移动到页面的顶部, 0是最上面
    js2 = "var q=document.documentElement.scrollTop=0"
    driver.execute_script(js2)
    time.sleep(3)

    # 将页面滚动条拖到左边, 10000是最左边
    js3 = "var q=document.documentElement.scrollLeft=10000"
    driver.execute_script(js3)
    time.sleep(3)

    # 将页面滚动条拖到右边, 10000是最右边
    js4 = "var q=document.documentElement.scrollLeft=0"
    driver.execute_script(js4)
    time.sleep(3)

    # 新开一个窗口，通过执行js来新开一个窗口
    js5 = 'window.open("https://mail.163.com");'
    driver.execute_script(js5)
    time.sleep(3)

    # 执行js，让滚轮向下滚动
    js6 = 'window.scrollTo(0, document.body.scrollHeight)'
    driver.execute_script(js6)
    print(driver.page_source)
    time.sleep(3)

    # 使用js脚本拖动到指定地方 todo 未运行成功
    target = driver.find_element(By.ID, "su")
    driver.execute_script("arguments[0].scrollIntoView();", target)

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
