# coding: utf-8

import json
from flask import Blueprint, request
from db.mogodb import dbtags, dbsequence, dbnotes, dbcontent
mod = Blueprint('ajax', __name__)

@mod.route('/add/tag', methods=['POST'])
def tag():
    form = request.form.get('data', '')
    form = json.loads(form)
    content = form.get('data')

    # 更新 Id
    seq = list(dbsequence.findquery({}, {'tagId': 1}))
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
    form = request.form.get('data', '')
    form = json.loads(form)
    content = form.get('content')
    tagId = int(form.get('tagId'))

    # 更新 Id
    seq = list(dbsequence.findquery({}, {'noteId': 1}))
    noteId = seq[0].get('noteId', 0)
    newNoteId = noteId + 1
    dbsequence.update({'noteId': noteId}, {"$set": {'noteId': newNoteId}})

    data = {
        'content': content,
        'tagId': tagId,
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
    form = request.form.get('data', '')
    form = json.loads(form)
    tagId = int(form.get('tagId', 0))
    if tagId == 0:  # 选中全部
        notes = list(dbnotes.findall())
    else:
        notes = list(dbnotes.findquery({'tagId': tagId}, {}))

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
    form = request.form.get('data', '')
    form = json.loads(form)
    tagId = int(form.get('tagId', 0))
    noteId = int(form.get('noteId', 0))
    content = form.get('content', '')

    notes = list(dbcontent.findquery({'noteId': noteId}, {}))

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

    content = list(dbcontent.findquery({'noteId': noteId}, {}))

    if not content:
        return json.dumps({'status': 1, 'result': 1, "data": "", "msg": u"不存在该笔记"})
    else:
        response = {
            'content': content[0].get('content', '')
        }

        return json.dumps({'status': 1, 'result': 1, "data": response, "msg": u"sucess"})
















