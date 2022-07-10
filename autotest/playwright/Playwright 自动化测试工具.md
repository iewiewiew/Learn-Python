[TOC]

---

<h1 align="center">Playwright 自动化测试工具</h1>

> By：weimenghua
> Date：2023.04.21
> Description：

**参考资料**  
[playwright 官网](https://playwright.dev/)    
[playwright 源码](https://github.com/microsoft/playwright)



## 一、playwright 介绍
### 1.1、简介
Playwright 是微软在 2020 年初开源的新一代自动化测试工具，它的功能类似于 Selenium、Pyppeteer 等，都可以驱动浏览器进行各种自动化操作。

### 1.2、特点
- Playwright 支持当前所有主流浏览器，包括 Chrome 和 Edge（基于 Chromium）、Firefox、Safari（基于 WebKit） ，提供完善的自动化控制的 API。
- Playwright 支持移动端页面测试，使用设备模拟技术可以使我们在移动 Web 浏览器中测试响应式 Web 应用程序。
- Playwright 支持所有浏览器的 Headless 模式和非 Headless 模式的测试。
- Playwright 的安装和配置非常简单，安装过程中会自动安装对应的浏览器和驱动，不需要额外配置 WebDriver 等。
- Playwright 提供了自动等待相关的 API，当页面加载的时候会自动等待对应的节点加载，大大简化了 API 编写复杂度。



## 二、playwright 环境搭建
### 2.1、基于 python 安装
```
更新 pip
pip install --upgrade pip

安装 playwright
pip install playwright

安装浏览器 chromium/cr, firefox/ff, webkit/wk 等
playwright install

安装浏览器 chromium
playwright install chromium

查看支持的浏览器 
playwright install --help
结果：Install custom browsers, supports chromium, chrome, chrome-beta, msedge, msedge-beta, msedge-dev, firefox, webkit.
```

### 2.2、基于 node.js 安装

```
使用 npm
npm init playwright@latest			    # 在当前目录下生成
npm init playwright@latest new-project	# 在 <new-project> 目录下生成

使用 yarn
yarn create playwright

PlayWright 会自动生成项目模版，结构如下：
playwright.config.ts    # PlayWright配置文件
package.json            # nodejs配置文件
package-lock.json       # nodejs配置锁定
tests/                  # 你指定的测试案例目录
  example.spec.ts       # 测试案例的一个模版，实际编写时候可以删掉
tests-examples/         # 样例目录
  demo-todo-app.spec.ts # 测试案例的样例

安装依赖
npm i -D @playwright/test

安装浏览器 chromium/cr, firefox/ff, webkit/wk
npx playwright install
```



## 三、playwright 实战
### 3.1、代码录制
python
```
浏览器指令录制
指令格式：playwright codegen [website]
指令示例：playwright codegen https://www.baidu.com

查看 codegen 用法
playwright codegen --help
```

nodejs
```
浏览器指令录制
指令格式：npx playwright codegen [website]
指令示例：npx playwright codegen https://www.baidu.com

将网站运行在不同的浏览器上
指令格式：npx playwright [browser] [website]
指令示例：npx playwright cr https://www.baidu.com
```

### 3.2、打开网站

```
模拟 iPhone 13 打开网站
playwright open --device="iPhone 13" https://www.baidu.com

屏幕大小和颜色主题
playwright open --viewport-size=800,600 --color-scheme=dark https://www.baidu.com

模拟地理位置、语言和时区
playwright open --timezone="Europe/Rome" --geolocation="41.890221,12.492348" --lang="it-IT" maps.google.com

模拟 iPhone 12 Pro 打开百度，使用 Chromium 驱动，生成的脚本语言设置为 python，保存名称为 test_playwright.py
playwright codegen --device="iPhone 12 Pro" -b chromium --target python -o test_playwright.py https://www.baidu.com
```

### 3.3、执行测试

```
执行所有测试
npx playwright test
等于
./node_modules/.bin/playwright test

执行指定的测试案例文件
npx playwright test example.spec.ts

执行一组测试案例（tests/todo-page/和tests/landing-page/两个目录下的所有案例）
npx playwright test tests/todo-page/ tests/landing-page/

执行测试案例文件名包含landing或者login的案例文件
npx playwright test landing login

执行测试案例的名称为”add a todo item”的
npx playwright test -g "add a todo item"

在“有头”模式下执行测试（就是会看到浏览器被打开，而默认的无头模式则不会看到有浏览器打开）
npx playwright test --headed

指定浏览器执行测试
npx playwright test landing-page.ts --project=chromium

调试测试案例
npx playwright test --debug

调试指定的测试案例脚本文件
npx playwright test example.spec.ts --debug

调试测试脚本文件指定行号的测试案例
npx playwright test example.spec.ts:10 --debug

展示测试报告
npx playwright show-report
```

### 3.4、教程
#### 创建浏览器对象

```
# 同步
# Can be "msedge", "chrome-beta", "msedge-beta", "msedge-dev", etc.
browser = playwright.chromium.launch(channel="chrome")

# 异步
# Can be "msedge", "chrome-beta", "msedge-beta", "msedge-dev", etc.
browser = await playwright.chromium.launch(channel="chrome")
```

#### 浏览器上下文

浏览器上下文对象是浏览器实例中一个类似于隐身模式的会话，简单说就是该上下文资源是完全独立的，与其他的上下文互不干扰，所以在自动化测试中，可以对每一个测试用例都单独开一个浏览器上下文。这对于多用户，多场景的测试非常有用。

```
# 同步
browser = playwright.chromium.launch()
context = browser.new_context()
page = context.new_page()

# 异步
browser = await playwright.chromium.launch()
context = await browser.new_context()
page = await context.new_page()
```

#### Page对象

一般来说，一个page对应一个浏览器选项卡。而Page对象的作用在于和页面的内容进行交互，以及导航和加载新的页面。

#### selector

```
playwright.$(selector)  # 定位到匹配的第一个元素
playwright.$$(selector)  # 定位到所有匹配的元素
playwright.selector(element)  # 给指定的元素生成selector
playwright.inspect(selector)  # 在 Elements 面板中显示元素（如果相应浏览器的 DevTools 支持它
playwright.locator(selector)  # 使用playwright内置的查询引擎来查询匹配的节点
playwright.highlight(selector)  # 高亮显示第一个匹配的元素
playwright.clear()  #取消现存的所有的高亮
```

#### 截图

```
playwright screenshot --help  # 查看帮助

# 模拟iPhone截图，等待3秒后截图，保存为twitter-iphone.png
playwright screenshot \
    --device="iPhone 11" \
    --color-scheme=dark \
    --wait-for-timeout=3000 \
    twitter.com twitter-iphone.png

# 全屏截图
playwright screenshot --full-page www.baidu.com baidu-full.png
```

#### 生成PDF

```
生成PDF（只有在无头模式下才能运行）
playwright pdf https:gitee.com gitee.pdf
```

#### 打开开发工具

```
chromium.launch(devtools=True)  # 同步
await chromium.launch(devtools=True)  # 异步
```

#### 模拟导航栏的功能

```python
page.goto(url, **kwargs) # 定向
page.reload(**kwargs) # 刷新
page.go_back(**kwargs)  # 后退
page.go_forward(**kwargs)  # 前进
```
