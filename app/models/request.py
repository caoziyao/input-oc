# coding: utf-8

class Request():
    """
    原始 http 请求
    """
    def __init__(self):
        self.method = ''
        self.url = ''
        self.protocol = ''
        self.headers = {}
        self.body = ''

