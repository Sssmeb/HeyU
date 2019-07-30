# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 14:10
# @Author  : CRJ
# @File    : chat.py
# @Software: PyCharm
# @Python3.6
from app.extensions import db
import datetime


class Chat(db.Model):
    __tablename__ = 'chat'
    from_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    to_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.DATETIME, default=datetime.datetime.utcnow)
    author = db.relationship('User')