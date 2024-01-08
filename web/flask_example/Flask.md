[TOC]

<h1 align="center">Flask</h1>

> By：weimenghua  
> Date：2024.01.17  
> Description：  

**参考资料**  
- [flask-admin](https://flask-admin.readthedocs.io/en/latest/)   
- [helloflask 电子书](https://tutorial.helloflask.com/)  
- [helloflask 源码](https://github.com/helloflask/watchlist)
- [readthedocs](https://dormousehole.readthedocs.io/en/latest/index.html)
- [test-platform-api](https://github.com/zhongyehai/test-platform-api)
- [flask-mega-tutorial](http://www.pythondoc.com/flask-mega-tutorial/index.html)
- [flask-tutorial](https://www.cainiaojc.com/flask/flask-tutorial.html)
- [Python+Flask+Vue，练手项目合集在这，跟着敲就是了](https://mp.weixin.qq.com/s/PR-CVN_zxtGj1CQmDciP6Q)
- [TestProjectManagement](https://github.com/QiCodeCN/TestProjectManagement)


@todo  
用 Flask 写一个 MockServer

 

### 基础

安装 flask 及扩展

```
pip install flask
pip install flask-login
pip install flask-openid
pip install flask-mail
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf
pip install flask-babel
pip install guess_language
pip install flipflop
pip install coverage
pip install python-dotenv
```

创建文件：`touch .env .flaskenv`

在 .env 填写：`FLASK_APP=flask_01.py`
启动应用：`flask run`，默认端口号：5000

在 .flaskenv 填写：`FLASK_DEBUG=1` 
开启调试模式：`flask run --debug`

使服务器被公开访问：`flask run --host=0.0.0.0`



### 入门
从 flask 包导入 Flask 类，通过实例化这个类，创建一个程序对象 app。 __name__ 是一个适用于大多数情况的快捷方式，有了这个参数， Flask 才能知道在哪里可以找到模板和静态文件等东西。
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'
   
app.run(host, port, debug, options)
```

参数说明

| 序号 | 参数与描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | **host** 要监听的主机名。默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用 |
| 2    | **port** 默认值为5000                                        |
| 3    | **debug** 默认为false。如果设置为true，则提供调试信息        |
| 4    | **options** 要转发到底层的Werkzeug服务器。                   |



### 路由

传入 app.route 装饰器的参数称为 URL 规则。一个视图函数也可以绑定多个 URL，这通过附加多个装饰器实现。

```
@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return "Hello Flask"
```

| 路由类型 | 实现方式                            |
| :------- | :---------------------------------- |
| 基本路由 | `@app.route('/')`                   |
| 动态路由 | `@app.route('/user/<username>')`    |
| 限定类型 | `@app.route('/post/<int:post_id>')` |



### 模板

创建模板目录：`mkdir templates`

Jinja2 通用模板

```
<h1>{{ username }}的个人主页</h1>
{% if bio %}
    <p>{{ bio }}</p>  {# 这里的缩进只是为了可读性，不是必须的 #}
{% else %}
    <p>自我介绍为空。</p>
{% endif %}  {# 大部分 Jinja 语句都需要声明关闭 #}
```

- {{ ... }} 用来标记变量。
- {% ... %} 用来标记语句，比如 if 语句，for 语句等。
- {# ... #} 用来写注释。



### 静态文件

创建静态文件目录：`mkdir static`



### 会话

```
app.secret_key = '123456'

response.set_cookie()
```



### 数据库

安装依赖：`pip install flask-sqlalchemy==2.5.1 sqlalchemy==1.4.47`

模型类要声明继承 db.Model。  
每一个类属性（字段）要实例化 db.Column，传入的参数为字段的类型，下面的表格列出了常用的字段类。  
在 db.Column() 中添加额外的选项（参数）可以对字段进行设置。比如，primary_key 设置当前字段是否为主键。除此之外，常用的选项还有 nullable（布尔值，是否允许为空值）、index（布尔值，是否设置索引）、unique（布尔值，是否允许重复值）、default（设置默认值）等。

常用的字段类型如下表所示：

| 字段类           | 说明                                          |
| :--------------- | :-------------------------------------------- |
| db.Integer       | 整型                                          |
| db.String (size) | 字符串，size 为最大长度，比如 `db.String(20)` |
| db.Text          | 长文本                                        |
| db.DateTime      | 时间日期，Python `datetime` 对象              |
| db.Float         | 浮点数                                        |
| db.Boolean       | 布尔值                                        |

执行：`flask shell` 进入控制台

初始化数据库：`flask initdb`

执行操作表数据：`flask forge`

测试接口：`curl -X POST -H "Content-Type: application/json" -d '{"title": "abc", "year": "2024"}' http://127.0.0.1:8888`



### 消息闪送

flash(message, category)：message 是要闪现的实际消息，category 可选。它可以是“error”，“info”或“warning”。

get_flashed_messages(with_categories, category_filter)：两个参数都是可选参数。如果接收到的消息具有类别，则第一个参数是元组。第二个参数仅用于显示特定消息。



### Flask-WTF

**WTforms**表单字段含义：

- TextField ：表示`<input type ='text'>` HTML表单元素
- BooleanField：表示`<input type ='checkbox'>` HTML表单元素
- DecimalField：用于显示带小数的数字的文本字段
- IntegerField：用于显示整数的文本字段
- RadioField：表示`<input type = 'radio'> `HTML表单元素
- SelectField：表示选择表单元素
- TextAreaField：表示`<textarea>` HTML表单元素
- PasswordField：表示`<input type = 'password'>` HTML表单元素
- SubmitField：表示`<input type = 'submit'>`表单元素

**validators：** 常用验证的使用：

- DataRequired：检查输入字段是否为空
- Email：检查字段中的文本是否遵循电子邮件ID约定
- IPAddress：在输入字段中验证IP地址
- Length：验证输入字段中的字符串的长度是否在给定范围内
- NumberRange：验证给定范围内输入字段中的数字
- URL：验证在输入字段中输入的URL



### uwsgi

安装
```
pip install uwsgi  
pip install uwsgi -I --no-cache-dir
```

新建 uwsgi.ini

运行 uWSGI 服务器
`uwsgi --ini uwsgi.ini`

后台执行
`uwsgi -d --ini uwsgi.ini`

指定参数运行
`uwsgi --http :8888 --wsgi-file app.py --callable app`

重启uwsgi
`uwsgi --reload uwsgi.pid`

停止uwsgi
`uwsgi --stop uwsgi.pid`

查看 Python 解释器路径
`which python3`

检查以下文件发现都不存在
```
ls /Library/Frameworks/Python3.framework
ls /System/Library/Frameworks/Python3.framework
```

执行 `python3` 进入 python 环境，输入 `import sys` 再输入 `sys.path`



### Flasgger

pip install flasgger
