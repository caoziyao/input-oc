# coding:utf-8
#!/user/bin/python

import os
from datetime import timedelta
from flask import Flask, render_template, Blueprint, redirect, session, g
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user
from config.constants import staticFolder, templateFolder
from app.myapp import register_blue
from app.models.user import User, Anonymous
from pymongo import MongoClient
from app.db.mongodb import db
dbsession = db['session']


app = Flask(__name__)
app.static_folder = staticFolder
app.template_folder = templateFolder

app.secret_key = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app=app)
login_manager.anonymous_user = Anonymous


# 从数据库加载 session
def upload_session():
    r = list(dbsession.find({'username': 'abc'}))
    g.g_session = r[0].get('sessionId', '') if r else ''
    if g.g_session:
        session['user_id'] = g.g_session
        session['userid'] = g.g_session


@app.before_request
def before_request():
    """
    请求 url 前判断是否登录
    :return:
    """
    upload_session()
    # 设置sessin的有效时间
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=500)


# @login_manager.unauthorized_handler  # 自定义未登录跳转
# def unauthorized():
#     print('loginurl',)
#     return redirect('user/login')


# 在每次请求过来后，Flask-Login都会从Session中寻找”user_id”的值，
# 如果找到的##话，就会用这个”user_id”值来调用此回调函数，并返回一个用户类对象
# 如果用户名存在则构建一个新的用户类对象
# 如果不存在，必须返回None
@login_manager.user_loader
def load_user(_id):
    u = User(_id)
    return u




def main():
    config = {
        'host': '0.0.0.0',
        'port': 8002,
        'debug': True
    }
    register_blue(app)
    app.run(**config)


if __name__ == '__main__':

    main()