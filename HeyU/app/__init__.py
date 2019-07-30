from app.setting import config
from flask import Flask
from app.extensions import db


def create_app(config_name=None):
    if config_name is None:
        config_name = 'development'

    app = Flask('app')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprint(app)
    register_errors(app)

    return app


def register_extensions(app):
    db.init_app(app)
    db.create_all(app=app)


def register_blueprint(app):
    # app.register_blueprint(xx)
    pass

def register_errors(app):
    pass