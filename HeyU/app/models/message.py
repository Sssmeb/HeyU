# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 14:09
# @Author  : CRJ
# @File    : message.py
# @Software: PyCharm
# @Python3.6
from app.extensions import db


class Message(db.Model):
    __tablename__ = 'message'
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
    content = db.Column(db.Text, nullable=False)
    # 信息的类型 文本、图片、等等 扩展
    # type_id = db.Column(db.SMALLINT, )
