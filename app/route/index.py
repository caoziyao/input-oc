# coding: utf-8

from flask import render_template, Blueprint
from app.db.mogodb import dbtags, dbnotes

mod = Blueprint('index', __name__)

@mod.route('/')
def index():
    tags = list(dbtags.findall())
    notes = list(dbnotes.findall())
    return render_template('index.html', tags=tags, notes=notes)