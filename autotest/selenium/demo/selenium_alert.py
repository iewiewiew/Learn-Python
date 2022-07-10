# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/23 21:23
@description  弹窗
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')
    time.sleep(3)

    # 进入百度设置页面
    driver.find_element(By.XPATH, "//*[@id='s-usersetting-top']").click()

    # 打开"搜索设置"
    driver.find_element(By.XPATH, "//*[@id='s-user-setting-menu']/div/a[1]").click()
    time.sleep(3)

    # 点击保存设置
    driver.find_element(By.XPATH, '//*[@id="se-setting-7"]/a[2]').click()
    time.sleep(3)

    # 等待5秒后判断是否弹出窗口出现
    WebDriverWait(driver, 5).until(EC.alert_is_present())

    print('打印弹窗内容：{}'.format(driver.switch_to.alert.text))

    # 接受弹窗
    driver.switch_to.alert.accept()

    # 关闭弹窗
    # driver.switch_to.alert.dismiss()

    time.sleep(3)

    # 关闭对话框后继续操作页面
    driver.find_element(By.ID, "kw").send_keys("selenium")

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    demo()
