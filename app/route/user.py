# coding:utf-8
#!/user/bin/python

import hashlib
import json
import random
import uuid
from flask import render_template, Blueprint, request, redirect, session
from flask_login import AnonymousUserMixin, LoginManager, UserMixin, login_required, current_user, login_user
from flask_login import logout_user
from app.share.util import md5, sh1hexdigest
from app.share.verifcode import gene_code


mod = Blueprint('user', __name__)


class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest2'

    @property
    def id(self):
        return 0

    @property
    def is_superuser(self):  # 超级用户
        return False

    @property
    def loginurl(self):
        urlrootpath = 'user/login'
        return urlrootpath


class User(UserMixin):
    """
    用户类
    """
    def __init__(self, _id):
        self.id = _id

    # 必须实现
    def get_id(self):
        """
        返回 id
        :return:
        """
        return self.id  # unicode(uuid.uuid4())



@mod.route('/randomcode', methods=['POST'])
def  randomcode():
    """

    :return:
    """
    pwd = uuid.uuid1()
    r = sh1hexdigest(str(pwd))

    return json.dumps(r)


@mod.route('/login', methods=['GET', 'POST'])
def login():
    method = request.method
    if method == 'GET':
        u = current_user
        print('u', u)
        return render_template('login.html')
    elif method == 'POST':
        username = request.form.get('username', '')
        u = User(username)
        login_user(u)

        return redirect('/todo')


@mod.route('/logout', methods=['GET'])
def logout():
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




