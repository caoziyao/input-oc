# coding: utf-8

from flask import render_template, Blueprint, redirect
from flask_login import current_user
from app.db.mogodb import dbtags, dbnotes

mod = Blueprint('index', __name__)

@mod.before_request
def before_request():
    if not current_user.is_authenticated:
        return redirect(current_user.loginurl)  # 没有认证返回登录页



@mod.route('/')
def index():
    tags = list(dbtags.findall())
    notes = list(dbnotes.findall())
    return render_template('index.html', tags=tags, notes=notes)