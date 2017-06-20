# coding:utf-8
#!/user/bin/python

import hashlib
import json
import random
import uuid
from flask import render_template, Blueprint, request, redirect, session
from flask_login import  current_user, login_user
from flask_login import logout_user
from app.share.util import  sh1hexdigest
from app.share.verifcode import gene_code
from app.models.user import User

from app.db.mongodb import db

mod = Blueprint('user', __name__)

dbsession = db['session']


def upload_session():
    r = list(dbsession.find({'username': 'abc'}))
    session['user_id'] = r[0].get('sessionId', '')
    session['userid'] = r[0].get('sessionId', '')
    print(r)




def save_session():

    session_id = session['userid']
    data = {
        'username': 'abc',
        'sessionId': session_id,
    }
    dbsession.insert(data)


def drop_session(session_id):

    dbsession.remove({'sessionId': session_id})


@mod.route('/randomcode', methods=['POST'])
def  randomcode():
    """
    特征值用于登录系统
    :return:
    """
    pwd = uuid.uuid1()
    r = sh1hexdigest(str(pwd))
    session['userid'] = r   # 记住登录id
    return json.dumps(r)


@mod.route('/login', methods=['GET', 'POST'])
def login():
    method = request.method
    if method == 'GET':
        upload_session()
        u = current_user
        print('u', u)
        a = session
        return render_template('login.html')
    elif method == 'POST':
        userid = request.form.get('username', '')
        u = User(userid)
        if userid == session['userid']:
            login_user(u, True)

            save_session()
            return redirect('/todo')
        else:
            return redirect('.')




@mod.route('/logout', methods=['GET'])
def logout():
    session_id = session['userid']
    drop_session(session_id)
    logout_user()
    return redirect(current_user.loginurl)


@mod.route('/verifcode', methods=['GET'])
def verifcode():
    code = gene_code()
    r = {
        'code': code,
    }
    session['verifycode'] = code  # 把验证码保存于session内,使用后需要del掉
    print('code', code)
    return json.dumps(r)



@mod.route('/check/verifycode', methods=['POST'])
def check_verifcode():
    data = json.loads(request.data)
    code = data.get('data')
    lower = session['verifycode'].lower()

    upper = session['verifycode'].upper()
    if code == lower or code == upper or code == session['verifycode']:
        r = {'result': 1, 'msg': '校验通过'}
        # del session['verifycode']
    else:
        r = {'result': 0, 'msg': '校验失败'}


    return json.dumps(r)




