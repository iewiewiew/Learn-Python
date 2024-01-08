# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/22 11:43
@description  Flask-WTF: 主要用于表单的处理验证

pip install flask-wtf
"""

from flask import Flask, flash, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('用户名: ', validators=[DataRequired('请输入用户名')])
    password = PasswordField('密码: ', validators=[DataRequired('请输入密码')])
    address = TextAreaField('地址: ')
    email = EmailField('邮箱: ', validators=[Length(10, 50)])
    remember = BooleanField('记住我')
    submit = SubmitField('提交')


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False #直接关闭
app.secret_key = 'secret_key'


@app.route('/login', methods=['post', 'get'])
def login():
    login_form = LoginForm()
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == 'admin':
        return 'login success'
    else:
        flash('参数有误或者不完整')
        return render_template('index12_flask_wtf.html', form=login_form)
    return render_template('index12_flask_wtf.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

    """
    测试链接：http://127.0.0.1:5000/login
    """