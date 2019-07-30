# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 14:03
# @Author  : CRJ
# @File    : user.py
# @Software: PyCharm
# @Python3.6
from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_online = db.Column(db.Boolean, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)