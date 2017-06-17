# coding:utf-8
#!/user/bin/python

from flask import render_template, Blueprint, request, redirect
from flask_login import AnonymousUserMixin, LoginManager, UserMixin, login_required, current_user, login_user
from flask_login import logout_user
import hashlib
import json
from app.share.util import md5, sh1hexdigest

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



@mod.route('/generate_code', methods=['POST'])
def  generate_code():
    """

    :return:
    """
    data = request.data
    c = json.loads(data)
    pwd = c.get('code', '')

    r = sh1hexdigest(pwd)

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


@mod.route('/logout')
def logout():
    logout_user()
    return redirect(current_user.loginurl)