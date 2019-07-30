# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 14:09
# @Author  : CRJ
# @File    : relation.py
# @Software: PyCharm
# @Python3.6
from app.extensions import db


class Relation(db.Model):
    __tablename__ = 'relation'
    user_id_a = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_b = db.Column(db.Integer, db.ForeignKey('user.id'))
    # type_id = db.Column(db.Integer, db.ForeignKey('type.id'))