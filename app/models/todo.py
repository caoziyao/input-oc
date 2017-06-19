# coding: utf-8

from app.share.constants import *



class Todo(object):
    """
    todo model
    """
    def __init__(self):
        self.create_time = ''
        self.update_time = ''
        self.name = ''
        self.content = ''
        self.id = ''
        self.status = CREATE_STATUS  # 默认新建状态


    def save(self):
        """
        保存
        :return:
        """
        pass
