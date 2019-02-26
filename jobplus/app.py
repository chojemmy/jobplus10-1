from flask import Flask, render_template
from flask_migrate import Migrate
from flask_login import LoginManger
from jobplus.config import configs
from jobplus.models import db, User

# 注册插件到app
def register_extensions(app):
    pass

def register_blueprints(app):
    from .handlers import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

def register_error_handlers(app):
    '''页面出错时，返回的信息'''
    pass


def create_app(config):
    '''app 工厂'''
    app = Flask(__name__)

    if isinstance(config, dict):
        app.config.update(config)
    else:
        app.config.from_object(configs.get(config, None))

    register_extensions(app)
    register_blurprints(app)
    register_error_handlers(app)

    return app

