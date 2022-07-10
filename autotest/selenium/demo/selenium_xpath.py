# !/usr/bin/env selenium
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2022/5/22 10:33
@description  xpath定位

常用方法： driver.find_element(By.XPATH, '//*[@属性=元素值]')
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.baidu.com")

    """
    标签及属性：<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
    父标签及属性：<span class="bg s_ipt_wr new-pmd quickdelete-wrap">
    """

    # 1、用XPATH通过id属性定位
    driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("selenium")

    # 2、用XPATH通过name属性定位
    driver.find_element(By.XPATH, "//*[@name='wd']").send_keys("selenium")

    # 3、用XPATH通过class属性定位
    driver.find_element(By.XPATH, "//*[@class='s_ipt']").send_keys("selenium")

    # 4、用XPATH通过其他属性定位
    driver.find_element(By.XPATH, "//*[@autocomplete='off']").send_keys("selenium")

    # 5、用XPATH通过text()定位
    driver.find_element(By.XPATH, '//*[text()="设置"]').click()

    time.sleep(3)
    driver.close()


def demo1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.baidu.com")

    # 用XPATH模糊匹配文本
    driver.find_element(By.XPATH, '//*[contains(text(),"hao")]').click()

    # 用XPATH模糊匹配属性
    driver.find_element(By.XPATH, '//*[contains(@id,"kw")]').send_keys("selenium")

    # 用XPATH模糊匹配属性以什么开头
    driver.find_element(By.XPATH, "//*[starts-with(text(),'hao')]").click()

    # 用XPATH模糊匹配属性以什么结尾 todo 运行不成功
    driver.find_element(By.XPATH, "//*[ends-with(text(),'123')]").click()

    # 用XPATH正则表达式 todo 运行不成功
    driver.find_element(By.XPATH, "//*[matchs(text(),'hao123')]").click()

    # 用XPATH通过标签名+属性定位
    driver.find_element(By.XPATH, "//input[@class='s_ipt']").send_keys("selenium")

    # 通过定位他爸爸来定位input输入框 todo 未执行成功
    # driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input").send_keys("selenium")
    driver.find_element(By.XPATH, "//span[@class='bg s_ipt_wr new-pmd quickdelete-wrap']/input").send_keys("selenium")

    # 通过定位他爷爷来定位input输入框
    driver.find_element(By.XPATH, "//form[@id='form']/span/input").send_keys("selenium")

    # 用XPATH逻辑运算
    driver.find_element(By.XPATH, "//*[@id='kw' and @autocomplete='off']").send_keys("selenium")

    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    demo()
