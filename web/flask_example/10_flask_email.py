# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/21 11:27
@description  邮件 注：未发送邮件成功

pip install Flask-Mail
"""

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '1425615649@qq.com'
app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route('/')
def index():
    msg = Message('Hello', sender='1425615649@qq.com', recipients=['1425615649@qq.com'])
    msg.body = 'Flask Email Body'
    return "Sent"


if __name__ == '__main__':
    app.run(debug=True)
