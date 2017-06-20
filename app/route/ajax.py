# coding: utf-8

import json
from flask import Blueprint, request
from app.db.mongodb import db

mod = Blueprint('ajax', __name__)

dbsequence = db['sequence']
dbtags = db['tags']
dbnotes = db['notes']
dbcontent = db['content']

@mod.route('/add/tag', methods=['POST'])
def tag():
    form = request.form.get('data', '')
    form = json.loads(form)
    content = form.get('data')

    # 更新 Id
    seq = list(dbsequence.find({}, {'tagId': 1}))
    tagId = seq[0].get('tagId', 0)
    newTagId = tagId + 1
    dbsequence.update({'tagId': tagId}, {"$set": {'tagId': newTagId}})

    data = {
        'content': content,
        'tagId': newTagId
    }

    dbtags.insert(data)

    response = {
        'content': content,
        'tagId': newTagId
    }

    return json.dumps({'status': 1, 'result': 1, "data": response, "msg": u"sucess"})


@mod.route('/add/note', methods=['POST'])
def note():
    """
    添加 notes
    :return:
    """
    form = request.form.get('data', '')
    form = json.loads(form)
    content = form.get('content')
    tagId = int(form.get('tagId'))

    # 更新 Id
    seq = list(dbsequence.find({}, {'noteId': 1}))
    noteId = seq[0].get('noteId', 0)
    newNoteId = noteId + 1
    dbsequence.update({'noteId': noteId}, {"$set": {'noteId': newNoteId}})

    data = {
        'content': content,
        'tagId': str(tagId),
        'noteId': newNoteId
    }
    dbnotes.insert(data)

    response = {
        'content': content,
        'noteId': newNoteId
    }
    return json.dumps({'status': 1, 'result': 1, "data": response, "msg": u"sucess"})


@mod.route('/select/notes', methods=['POST'])
def select():
    """
    查询 notes
    :return:
    """
    form = request.form.get('data', '')
    form = json.loads(form)
    tagId = int(form.get('tagId', 0))
    if tagId == 0:  # 选中全部
        notes = list(dbnotes.find())
    else:
        notes = list(dbnotes.find({'tagId': tagId}))

    response = []
    for note in notes:
        da = {
            'content': note.get('content'),
            'tagId': note.get('tagId'),
            'noteId': note.get('noteId')
        }
        response.append(da)

    return json.dumps({'status': 1, 'result': 1, "data": response, "msg": u"sucess"})


@mod.route('/note/save', methods=['POST'])
def save():
    """
    保存 note
    :return:
    """
    form = request.form.get('data', '')
    form = json.loads(form)
    tagId = int(form.get('tagId', 0))
    noteId = int(form.get('noteId', 0))
    content = form.get('content', '')

    notes = list(dbcontent.find({'noteId': noteId}))

    if not notes:
        da = {
            'tagId': tagId,
            'noteId': noteId,
            'content': content
        }
        dbcontent.insert(da)
    else:
        dbcontent.update({'noteId': noteId}, {"$set": {'content': content}})

    return json.dumps({'status': 1, 'result': 1, "data": "", "msg": u"sucess"})


@mod.route('/add/content', methods=['POST'])
def addcontent():
    form = request.form.get('data', '')
    form = json.loads(form)
    noteId = int(form.get('noteId', 0))

    content = list(dbcontent.find({'noteId': noteId}))

    if not content:
        return json.dumps({'status': 1, 'result': 1, "data": "", "msg": u"不存在该笔记"})
    else:
        response = {
            'content': content[0].get('content', '')
        }

        return json.dumps({'status': 1, 'result': 1, "data": response, "msg": u"sucess"})
















