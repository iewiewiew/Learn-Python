# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2023/4/8 12:21
@description  测试百度
"""

from time import sleep
from playwright.sync_api import sync_playwright


class TestDemo():
    def setup(self):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def teardown(self):
        self.browser.close()

    def test_click(self):
        self.page.goto("https://www.baidu.com")

        self.page.click('id=s-top-loginbtn')

        with self.context.expect_page() as new_page_info:
            self.page.click('"立即注册"')  # Opens a new tab
        register_page = new_page_info.value

        register_page.wait_for_load_state()
        print(register_page.title())

        # 注册用户名密码
        register_page.fill("id=TANGRAM__PSP_4__userName", "username")
        register_page.fill("id=TANGRAM__PSP_4__phone", "12345678")
        register_page.close()
        sleep(2)

        # 登录用户名密码
        self.page.fill("id=TANGRAM__PSP_11__userName", "username")
        self.page.fill("id=TANGRAM__PSP_11__password", "pwd")
        sleep(2)
