# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 14:03
# @Author  : CRJ
# @File    : setting.py
# @Software: PyCharm
# @Python3.6


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/heyu'


config = {
    'development': DevelopmentConfig
}