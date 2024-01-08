# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author       weimenghua
@time         2024/1/18 18:06
@description  表单
"""

from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


# 创建数据库模型
class User(db.Model):  # 自动生成小写表名：user
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')

        """
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('index'))
        """

        movie = Movie(title=title, year=year)
        db.session.add(movie)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('index'))

    movies = Movie.query.all()
    return render_template('index6_flask_form.html', movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
