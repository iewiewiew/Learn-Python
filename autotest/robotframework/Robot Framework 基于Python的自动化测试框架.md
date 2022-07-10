[TOC]

<h1 align="center">Robot Framework 基于Python的自动化测试框</h1>

> By:weimenghua
> Date：2022.07.10
> Description：

**参考资料**  
[rf官网](https://robotframework.org/)  
[rf中文手册](https://robotframework-userguide-cn.readthedocs.io/zh_CN/latest/)


## 一、简介
Robot Framework 基于Python的自动化测试框架，以下简称rf。



## 二、环境搭建
1. 安装nodejs
2. 安装python
3. 安装rf相关依赖库
pip install -U robotframework  
pip install -U robotframework-ride  #安装robotframework-ride生成RIDE快捷键
pip install -U --pre robotframework-ride
pip install -U https://github.com/robotframework/RIDE/archive/master.zip 
pip install -U robotframework-browser
pip install -U robotframework-requests
pip install -U robotframework-appiumlibrary 
pip install -U robotframework-seleniumlibrary  #web端自动化依赖插件
pip install -U robotframework-databaselibrary  #操作数据库
pip install -U robotframework-ExcelLibrary  #操作excel
pip install -U wxpython  #支持python图形化界面，主要用来运行RIDEwxPython
pip install -U pygments  #代码高亮库



## 三、运行robot
### 3.1、PyCharm编辑器
- PyCharm安装插件：File–>Settings–>Plugins, 搜索IntelliBot、Robot Framework Support等插件进行安装并重启PyCharm  
- 设置测试套件参数：File–>Settings->Tools->External Tools, 新增一个tool, 参数如下：
```
Name：Robot Run TestSuite(可自定义)  
Program：D:\workspace\PycharmProjects\Learn-Python\venv\Scripts\robot.exe  # 注：需在venv安装库, 并且指定robot.exe
arguments：-d log $FileName$ | -d results $FileName$  # 如果"|"转换错误, 可只填写：-d results $FileName$
working directory：$FileDir$  
```
- robot文件设置：File->Settings->Editor->File Types->Robot Feature Files添加 *.robot
- 运行robot配置：在PyCharm右上角点击Edit Configurations, Interpreter options：-m robot robot_demo.robot, Working directory：自定义
- 运行robot文件：在robot文件右键 -> External Tools, 选择robot文件运行

### 3.2、RIDE编辑器
1. 启动RIDE
方式一：双击RIDE图标即可启动, 前提：创建RIDE快捷键  
D:\software\PythonProjects\Learn-Python\venv\Scripts\pythonw.exe  -c "from robotide import main; main()" (原自动创建)
D:\software\Python37\pythonw.exe -c "from robotide import main; main()" (创建后点击无反应)
方式二： cmd进入D:\software\PythonProjects\Learn-Python\venv\Scripts, 执行：python ride.py
2. 新建project
3. 新建testsuit
4. 新建testcase
5. RIDE功能介绍
RIDE页面
![](./imgs/RIDE_DEMO.png)
RIDE文本页面
![](./imgs/RIDE_TEXT_DEMO.png)
   
### 3.3、练习项目
https://gitee.com/linlinjava/litemall.git  
启动后端：运行litemall-all的Application  
启动前端：进入litemall-all执行：cnpm install, cnpm run dev  
本地Swagger文档链接：http://localhost:8080/swagger-ui.html    
登录接口：http://122.51.199.160:8080/#/login


## 四、教程
web自动化的几个常用的关键字
- Open Browser 打开浏览器
- Maximize Browser Window 最大化浏览器
- Close All Browsers 关闭浏览器
- Input Text 文本框输入
- Click Element 点击元素
- Sleep 设置等待时长

踩坑：使用SeleniumLibrary而不是Selenium2Library


运行robot文件
python 
D:\software\PythonProjects\Learn-Python\venv\Scripts\robot.exe -d result robot_suit.robot
D:\software\Python37\Scripts\robot.exe -d result robot_suit.robot

执行单个robot：robot -d result robot_mall.robot
