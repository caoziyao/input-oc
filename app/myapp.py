# coding: utf-8
# 注册蓝图
from app.route import index, ajax


def register_blue(app):
    app.register_blueprint(ajax.mod, url_prefix='/ajax')  # ajax
    app.register_blueprint(index.mod)   # index


