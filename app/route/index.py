# coding: utf-8

from flask import render_template, Blueprint
from db.mogodb import dbuser

mod = Blueprint('index', __name__)

@mod.route('/')
def index():
    name = dbuser.findall()
    return render_template('index.html', name=name)