# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 14:03
# @Author  : CRJ
# @File    : heyu.py
# @Software: PyCharm
# @Python3.6

from flask import render_template
from app import create_app
app = create_app()


@app.route('/')
def hello_world():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
