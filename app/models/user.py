# coding: utf-8

import hashlib
import json
import random
import uuid
from flask import render_template, Blueprint, request, redirect, session
from flask_login import AnonymousUserMixin, LoginManager, UserMixin, login_required, current_user, login_user
from flask_login import logout_user
from app.share.util import md5, sh1hexdigest
from app.share.verifcode import gene_code


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