# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/17 14:06
@description  模拟键盘操作
"""

from time import sleep
from playwright.sync_api import sync_playwright


class TestInput():
    def setup(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def teardown(self):
        self.browser.close()

    def test_click(self):
        self.page.goto("https://sahitest.com/demo/clicks.htm")
        self.page.click('"click me"')
        self.page.dblclick('"dbl click me"')
        self.page.click('"right click me"', button='right')
        self.page.click('"right click me"', modifiers=["Shift"])
        self.page.hover('"Clear"')
        self.page.hover('"Clear"')
        self.page.click('"Clear"', position={'x': 0, 'y': 0})
        sleep(5)
