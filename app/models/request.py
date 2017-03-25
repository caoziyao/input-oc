# coding: utf-8


class Request():
    """
    原始 http 请求
    """
    def __init__(self):
        self.method = ''
        self.url = ''       # /static?file=zhihu.js
        self.protocol = ''
        self.headers = {}
        self.body = ''
        self.path = ''      # /static
        self.query = {}     # {file: zhihu.js}
        self.Cookie = {}    # Cookie:username=xxx

    def add_cookies(self):
        """
        解析出 cookie
        :param headersDict:
        :return:
        """
        cookies = self.headers.get('Cookie', '')
        kvs = cookies.split('; ')
        for kv in kvs:
            if '=' in kv:
                k, v = kv.split('=')
                self.Cookie[k] = v



