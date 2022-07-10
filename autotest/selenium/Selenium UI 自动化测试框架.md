[TOC]

<h1 align="center">Selenium UI 自动化测试框架</h1>

> By：weimenghua
> Date：2022.07.10
> Description：



## 一、搭建环境
1. 查看谷歌浏览器版本和安装路径：chrome://version/
2. 根据谷歌浏览器版本下载对应的chromedriver, chromedriver下载地址：http://chromedriver.storage.googleapis.com/index.html  
3. 安装Python
4. 把下载好的chromedriver放到Chrome的Application目录下和python安装路径下
5. 安装selenium：pip install selenium



## 二、webdriver 的工作流程

1. WebDriver 启动目标浏览器, 并绑定到指定端口。该启动的浏览器实例, 做为 WebDriver 的 remote server。
2. Client 端通过 CommandExcuter 发送 HTTPRequest 给 remote server 的侦听端口（通信协议： the webriver wire protocol）
3. Remote server 需要依赖原生的浏览器组件（如：IEDriverServer.exe、chromedriver.exe）, 来转化转化浏览器的 native 调用。



## 三、教程

### 元素定位

**webdriver提供了八种元素定位方法**

1. id
2. name
3. class name
4. tag name
5. link text
6. partial link text
7. xpath
8. css selector

**在Python语言中对应的定位方法**

1. find_element_by_id()                 #通过元素id定位
2. find_element_by_name()               #通过元素name定位
3. find_element_by_class_name()         #通过类名进行定位
4. find_element_by_tag_name()           #通过标签定位
5. find_element_by_link_text()          #通过完整超链接定位, find_element_by_link_text()方法通过元素标签对之间的文本信息来定位元素。不过, 需要强调的是Python 对于中文的支持并不好, 如查 Python 在执行中文的地方出现在乱码, 可以在中文件字符串的前面加个小“u”可以有效的避免乱码的问题, 加 u 的作用是把中文字符串转换中 unicode 编码, 如：find_element_by_link_text(u"新闻")。
6. find_element_by_partial_link_text()  #通过部分链接定位
7. find_element_by_xpath()              #通过xpath表达式定位
8. find_element_by_css_selector()       #通过css选择器进行定位

### 控制浏览器常用方法

1. set_window_size()	       #设置浏览器的大小
2. back()                      #控制浏览器后退
3. forward()                   #控制浏览器前进
4. refresh()                   #刷新当前页面
5. clear()                     #清除文本
6. send_keys (value)           #模拟按键输入
7. click()                     #单击元素
8. submit()                    #用于提交表单
9. get_attribute(name)         #获取元素属性值
10. is_displayed()             #设置该元素是否用户可见
11. size                       #返回元素的尺寸
12. text                       #获取元素的文本

### 鼠标事件

1. ActionChains(driver)	       #构造ActionChains对象
2. context_click()             #执行鼠标悬停操作
3. move_to_element(above)      #右击
4. double_click()              #双击
5. drag_and_drop()             #拖动
6. move_to_element(above)      #执行鼠标悬停操作
7. context_click()             #用于模拟鼠标右键操作， 在调用时需要指定元素定位
8. perform()                   #执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作

### 键盘事件

1. send_keys(Keys.BACK_SPACE)	#删除键（BackSpace）
2. send_keys(Keys.SPACE)	    #空格键(Space)
3. send_keys(Keys.TAB)	        #制表键(Tab)
4. send_keys(Keys.ESCAPE)	    #回退键（Esc）
5. send_keys(Keys.ENTER)	    #回车键（Enter）
6. send_keys(Keys.CONTROL,‘a')	#全选（Ctrl+A）
7. send_keys(Keys.CONTROL,‘c')	#复制（Ctrl+C）
8. send_keys(Keys.CONTROL,‘x')	#剪切（Ctrl+X）
9. send_keys(Keys.CONTROL,‘v')	#粘贴（Ctrl+V）
10. send_keys(Keys.F1…Fn)	    #键盘 F1…Fn



## 四、常见问题

**WebDriver中有哪些不同的等待类型？**

1. 显式等待：WebDriverWait() 显式等待的等待时间是固定的, 固定了10s就必须等待10s。显式等待仅适用于特定实例, 用于中止当前执行, 直到满足特定条件的元素出现为止（在允许的时间内）。
2. 隐式等待：implicitly_wait() 隐式等待的等待时间是个范围, 例如最大10s, 那么如果在3s的时候程序达到预期的结果, 那么就不在继续后面的7秒, 直接进入下一步操作, 而如果超出10s还没有相应, 程序就会报出相应的错误。

**driver.close() 和driver.quit() 有什么区别？**

1. driver.close()：关闭用户当前正在使用的Web浏览器窗口, 即WebDriver当前正在访问的窗口。close() 方法既不需要任何参数, 也无任何返回值。
2. driver.quit()：不同于close(), quit()方法用于关闭程序已打开的所有窗口。该方法也不需要任何参数, 也无任何返回值。
