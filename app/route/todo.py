# coding: utf-8


from flask import render_template, Blueprint, current_app, redirect
from flask_login import current_user


mod = Blueprint('todo', __name__)

@mod.before_request
def before_request():
    if not current_user.is_authenticated:
        return redirect(current_user.loginurl)  # 没有认证返回登录页

@mod.route('/')
def index():

    user = current_user
    user_id = user.id

    return render_template('todo_index.html')