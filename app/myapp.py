# coding: utf-8
# 注册蓝图
from app.route import index


def register_blue(app):
    app.register_blueprint(index.mod)   # index


