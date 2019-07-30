# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 14:03
# @Author  : CRJ
# @File    : extensions.py
# @Software: PyCharm
# @Python3.6

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))
