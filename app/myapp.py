# coding: utf-8
# 注册蓝图
from app.route import index, ajax, todo, user


def register_blue(app):
    app.register_blueprint(ajax.mod, url_prefix='/ajax')  # ajax
    app.register_blueprint(index.mod)   # index
    app.register_blueprint(todo.mod, url_prefix='/todo')  # todo
    app.register_blueprint(user.mod, url_prefix='/user')  # user


