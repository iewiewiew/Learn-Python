import re

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://e.gitee.com/yierdeyuzhou/code/repos")
    page.goto("https://gitee.com/login?redirect_to_url=https%3A%2F%2Fe.gitee.com%2Fyierdeyuzhou%2Fcode%2Frepos")
    page.get_by_placeholder("手机／邮箱／个人空间地址").click()
    page.get_by_placeholder("手机／邮箱／个人空间地址").fill("1425615649@qq.com")
    page.get_by_placeholder("请输入密码").click()
    page.get_by_placeholder("请输入密码").press("CapsLock")
    page.get_by_placeholder("请输入密码").fill("password")
    page.get_by_role("button", name="登 录").click()
    page.get_by_text("新建仓库新建仓库转入仓库导入 Github / Gitlab 仓库").click()
    page.get_by_role("option", name="新建仓库").click()
    page.locator("div").filter(has_text=re.compile(r"^仓库名称$")).get_by_role("textbox").click()
    page.locator("div").filter(has_text=re.compile(r"^仓库名称$")).get_by_role("textbox").fill("test-demo-004")
    page.wait_for_timeout(5000)
    page.locator("title").wait_for()  # 等待直到title元素被加载完全
    page.get_by_role("button", name="新建").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
