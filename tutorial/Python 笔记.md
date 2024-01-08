[TOC]

<H1 align="center">Python 笔记</H1>

> By：weimenghua
> Date：2023.08.14
> Description：

**参考资料**  
[python tutorial](https://docs.python.org/zh-cn/3/tutorial/index.html)  
[Python-100-Days](https://github.com/jackfrued/Python-100-Days)  
[Python-Core-50-Courses](https://github.com/jackfrued/Python-Core-50-Courses)  
[Python-Interview-Bible](https://github.com/jackfrued/Python-Interview-Bible)  
[awesome-python](https://github.com/vinta/awesome-python)  
[Python Example](https://www.programcreek.com/python/)



## 一、Python 环境搭建
```
查看 Python 版本
python --version
python3 --version

查看 Python 安装路径  
方式一
which python3  

方式二
在控制台输入：python3，进入交互页面输入
import sys
sys.path
输入 exit() 推出交互页面
```

**依赖管理 pip**

pip 是 Python 的软件包管理系统，Python 语言自带的命令行工具，它可以安装和管理第三方软件包。

```
升级 pip（-U 是更新的意思）
python -m pip install -U pip 

查看已安装模块
pip list

查看某个包的安装信息
pip show requests
```

**安装依赖**

requirements.txt 可以通过 pip 命令自动生成和安装，这种情况更适用于此项目是单独的虚拟 python 环境生成 requirements.txt 文件

```
pip install + 模块名称安装
pip install requests

生成 requirements.txt 文件
pip freeze > requirements.txt

从 requirements.txt 安装依赖
pip install -r requirements.txt

指定镜像源从 requirements.txt 安装依赖
pip install -i https://pypi.doubanio.com/simple/  -r requirements.txt

pip install win32con -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
-i https://pypi.doubanio.com/simple/   ------表示使用豆瓣源 （-i == --index-url）
--trusted-host pypi.doubanio.com       ------表示添加信任
```

**卸载依赖**

```
pip uninstall + 模块名称删除
举例：pip uninstall requests

从 requirements.txt 卸载依赖
pip uninstall -r requirements.txt
```

**更新 pip 镜像源**

```
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple some-package 
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

**国内 pip 镜像源**

- 阿里云 http://mirrors.aliyun.com/pypi/simple/ 
- 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
- 豆瓣(douban) http://pypi.douban.com/simple/ 
- 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
- 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
- pypi https://pypi.org/simple/  （Python 包索引: https://pypi.org）



## 二、Python 系列教程
### 01. 数据类型
**不可变数据**
- Number（数字）
- String（字符串）
- Tuple（元组）

**可变数据**
- List（列表）
- Dictionary（字典）
- Set（集合）

**举例**
- num = 123                                  
- str = "张三"                                 
- tup = ("张三", "李四", "王五")                
- lis = ['a', 'b', 'c', 1, 2]                
- dic = {'name': 'zhangsan', 'age': 18, 'city': 'beijing'}
- set = {'a', 'b', 'c', 'd', 'd'} 

### 02. 循环结构

### 03. 函数模块

### 04. 异常处理

### 05. 面向对象

把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。

### 06. 并发编程

### 07. 文件操作

### 08. 常用注解

### 09. 综合信息

**序列化和反序列化**

表1：JavaScript 数据类型（值）对应的 Python 数据类型（值）

| JSON         | Python       |
| ------------ | ------------ |
| `object`      |`dict`|
| `array`      |`list`|
| `string`     | `str`        |
| `number ` |`int` / `float`|
| `number` (real)   |`float`|
| `boolean` (`true` / `false`) | `bool` (`True` / `False`) |
| `null`       | `None`       |

表2：Python 数据类型（值）对应的 JavaScript 数据类型（值）

| Python                      | JSON                         |
| --------------------------- | ---------------------------- |
| `dict`                      | `object`                     |
| `list` / `tuple`            | `array`                      |
| `str`                       | `string`                     |
| `int` / `float`             | `number`                     |
| `bool` （`True` / `False`） | `boolean` (`true` / `false`) |
| `None`                      | `null`                       |



## 三、Python 零散记录

### 命名规范

[如何使用PEP8写出漂亮的Python代码](https://mp.weixin.qq.com/s/xU8fFQ6sKmd8CNozHG4ltg)

1. 项目名称首字母大写+大写式驼峰，ProjectName  
2. 模块名和包名全部小写+下划线驼峰 module_name，package_name  
3. 类名称，异常首字母大写+大写式驼峰，class ClassName:ExceptionName  
4. 全局变量、常量全部使用大写字母+下划线驼峰 GLOBAL_VAR_NAME，CONSTANT_NAME  
5. 方法名，函数名，其余变量，参数，实例全部小写+下划线驼峰 method_name，function_name，instance_var_name, function_parameter_name, local_var_name  
6. 处理计数器外，不使用单字母命名 

| 类型 | 命名约定                                                     | 例子                                            |
| ---- | ------------------------------------------------------------ | ----------------------------------------------- |
| 函数 | 使用小写字母。用下划线分隔单词以提高可读性。                 | function, python_function                       |
| 变量 | 使用小写字母、单词或词组。用下划线分隔单词以提高可读性。     | x, var, python_variable                         |
| 类   | 每个单词的开头字母都大写，不要用下划线分隔单词，这种格式叫做驼峰式或帕斯卡式。 | Model, PythonClass                              |
| 方法 | 使用小写字母。用下划线分隔单词以提高可读性。                 | class_method, method                            |
| 常数 | 使用大写字母、单词或词组。用下划线分隔单词以提高可读性。     | CONSTANT, PYTHON_CONSTANT, PYTHON_LONG_CONSTANT |
| 模块 | 使用短小、小写的单词或词组。用下划线分隔单词以提高可读性。   | module.py, python_module.py                     |
| 包   | 使用短小、小写的单词或词组。不要用下划线分隔单词。           | package, pythonpackage                          |

PEP 8（Python官方风格指南）倡导用不同的命名风格来命名 Python 中不同的标识符

1. 变量、函数和属性应该使用小写字母来拼写，如果有多个单词就使用下划线进行连接
2. 类中受保护的实例属性，应该以一个下划线开头
3. 类中私有的实例属性，应该以两个下划线开头
4. 类和异常的命名，应该每个单词首字母大写
5. 模块级别的常量，应该采用全大写字母，如果有多个单词就用下划线进行连接
6. 类的实例方法，应该把第一个参数命名为`self`以表示对象自身
7. 类的类方法，应该把第一个参数命名为`cls`以表示该类自身

PEP 8 的一些规定：
- 使用 4 个空格缩进，不要使用制表符。
- 每行代码长度不超过 79 个字符，对于长的表达式应适当换行。
- 在运算符前后加上空格，但不要过度空格化。
- 使用全小写字母和下划线命名变量、函数和模块。
- 在函数之间空一行，类之间空两行，使代码结构更清晰。

**Linter工具：规范代码自动化检查**
安装 Flake8：pip install flake8
在命令行中运行 Flake8： flake8 your_code.py

**Black：自动化代码格式化**
安装 Black：pip install black
在命令行中运行 Black： black your_code.py

### 常用库

> 标准库：sys / os / re / math / random / logging / json / pickle / shelve / socket / datetime / hashlib / configparser / urllib / itertools / collections / functools / threading / multiprocess / timeit / atexit / abc / asyncio / base64 / concurrent.futures / copy / csv / operator / enum / heapq / http / profile / pstats / ssl / unittest / uuid  
>
> 三方库：openpyxl / xlrd / xlwt / PyPDF2 / ReportLab / PyYAML / jieba / pillow / requests / urllib3 / responses / aiohttp / BeautifulSoup4 / lxml / pyquery / PyMySQL / psycopg2 / redis / PyMongo / Peewee / SQLAlchemy / alipay / PyJWT / itsdangerous / celery / flower / elasticsearch-dsl-py / PyCrypto / Paramiko / logbook / nose / pytest / coverage / Selenium / lineprofiler / memoryprofiler / matplotlib / pygal / OpenCV

### 生成可执行文件

pyinstaller -F demo.py

- -F pyinstaller -F demo.py 只在 dist 中生产一个 demo.exe 文件。
- -D pyinstaller -D demo.py 默认选项，除了 demo.exe 外，还会在在 dist 中生成很多依赖文件，推荐使用。
- -c pyinstaller -c demo.py 默认选项，只对 windows 有效，使用控制台，就像编译运行 C 程序后的黑色弹窗。
- -w pyinstaller -w demo.py 只对 windows 有效，不使用控制台。
- -p pyinstaller -p D:\python\Lib\site-packages demo.py 设置导入路径，一般用不到。
- -i pyinstaller -i D:\file.icon demo.py 将 file.icon 设置为 exe 文件的图标，推荐一个 icon 网站:icon

### 零散记录

1、is 和==的区别  
is 比较的是两个对象的地址值，也就是说两个对象是否为同一个实例对象  
==比较的是对象的值是否相等，其调用了对象的__eq__()方法

Auto PY to EXE 是一个基于 Eel 和 PyInstaller 构建的简单工具，将 Python 程序转换为可执行的 exe 文件
pip install auto-py-to-exe
auto-py-to-exe


查看 Python 所在路径
which python

查看当前系统上可用的 Python 版本
ls /usr/local/bin/python*

创建一个指向所选 Python 版本的符号链接
sudo ln -sf /usr/local/bin/python3.12 /usr/local/bin/python

查看当前 Python 版本
python --version

将默认 Python 版本还原为系统默认设置
sudo rm /usr/local/bin/python

查看 /usr/local/bin/python 的依赖
otool -L /usr/local/bin/python