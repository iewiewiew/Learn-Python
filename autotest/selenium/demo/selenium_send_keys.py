# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/21 22:08
@description  键盘操作

send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
send_keys(Keys.SPACE) 空格键(Space)
send_keys(Keys.TAB) 制表键(Tab)
send_keys(Keys.ESCAPE) 回退键（Esc）
send_keys(Keys.ENTER) 回车键（Enter）
send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
send_keys(Keys.F1) 键盘 F1
……
send_keys(Keys.F12) 键盘 F12
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(1)

    # 输入框输入内容
    driver.find_element(By.ID, "kw").send_keys("seleniumm")
    time.sleep(1)

    # 删除多输入的一个 m
    driver.find_element(By.ID, "kw").send_keys(Keys.BACK_SPACE)
    time.sleep(1)

    # 输入空格键+“教程”
    driver.find_element(By.ID, "kw").send_keys(Keys.SPACE)
    time.sleep(1)

    driver.find_element(By.ID, "kw").send_keys(u"教程")
    time.sleep(1)

    # ctrl+a 全选输入框内容
    driver.find_element(By.ID, "kw").send_keys(Keys.CONTROL, 'a')
    time.sleep(1)

    # ctrl+x 剪切输入框内容
    driver.find_element(By.ID, "kw").send_keys(Keys.CONTROL, 'x')
    time.sleep(1)

    # ctrl+v 粘贴内容到输入框
    driver.find_element(By.ID, "kw").send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 通过回车键盘来代替点击操作
    driver.find_element(By.ID, "su").send_keys(Keys.ENTER)

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
