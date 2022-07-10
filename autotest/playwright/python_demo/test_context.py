# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/11 12:30
@description  浏览器上下文
"""

# 同步模式
from playwright.sync_api import sync_playwright


def run(playwright):
    # 创建一个浏览器实例
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, slow_mo=500)

    # 创建两个浏览器上下文
    user_context = browser.new_context()
    admin_context = browser.new_context()

    # 创建选项卡和上下文之间的交互


with sync_playwright() as playwright:
    run(playwright)
