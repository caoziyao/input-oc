# coding: utf-8

import socket
import _thread
from util import log, error
from models.request import Request
from route.todo import route_todo
from route.zhihu import route_zhihu, route_static
from route.api.weather import route_api
from route.login import route_ajax

port = 8081
host = ''  # '' 代表接收任意 ip

class Server():
    """
    服务端
    """

    def __init__(self, host='', port=5000):
        try:
            addr = (host, port)
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(addr)
            self.socket.listen(5)
        except Exception as e:
            log('error', e)
            self.socket.close()

    def accept(self):
        return self.socket.accept()

    def close(self):
        self.socket.close()



def response_for_path(path, request):
    """根据 path 回应客户端"""
    # static?file=zhihu.js
    r = {
        '/static': route_static,
    }
    r.update(route_todo)
    r.update(route_api)
    r.update(route_zhihu)
    r.update(route_ajax)
    """
    根据 path 调用相应的处理函数
    没有处理的 path 会返回 404
    """
    response = r.get(path, error)
    return response(request)


def parsed_headers(headers):
    """ 解析 headers """
    query = {}
    for h in headers:
        k, v = h.split(': ', 1)
        query[k] = v
    return query


def parsed_url(url):
    # /static?file=zhihu.js&author=gua
    """
    {
        'file': 'zhihu.js',
        'author': 'gua'
    }
    """
    index = url.find('?')
    if index == -1:
        return url, {}
    else:
        path, query_string = url.split('?')
        args = query_string.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = v
        return path, query


def parsed_request(r):
    """第一步解析整个请求
    返回 method header body
    """
    request = Request()
    request.method = r.split()[0]
    request.url = r.split()[1]
    request.protocol = r.split()[2]
    headers = r.split('\r\n\r\n', 1)[0].split('\r\n')[1:]
    request.body = r.split('\r\n\r\n', 1)[1]
    request.headers = parsed_headers(headers)
    # 解析出 cookie
    request.add_cookies()
    # log(request.__dict__)

    # /static?file=zhihu.js&author=gua
    request.path, request.query = parsed_url(request.url)

    # log('request 请求:\r\n{}'.format(r))
    return request


def process_request(connection):
    """ 接收处理数据线程"""
    r = connection.recv(1024)
    r = r.decode('utf-8')
    # 因为 chrome 会发送空请求导致 split 得到空 list
    # 所以这里判断一下防止程序崩溃
    if len(r.split()) < 2:
        connection.close()
        return

    request = parsed_request(r)
    response = response_for_path(request.path, request)
    connection.sendall(response.encode(encoding='utf-8'))

    # print(response.encode(encoding='utf-8'))
    connection.close()



def run(host='', port=3001, debug=False):
    """
    启动服务器
    """
    s = Server(host, port)
    while True:
        # 接收一个连接
        connection, addr = s.accept()
        log('connection from {}'.format(addr))
        # 开一个新的线程来处理请求, 第二个参数是传给新函数的参数列表, 必须是 tuple
        # tuple 如果只有一个值 必须带逗号
        _thread.start_new_thread(process_request, (connection,))


if __name__ == '__main__':
    config = dict(
        host='',
        port=3000,
        debug=True,
    )
    run(**config)

"""
GET / HTTP/1.1
Host: 127.0.0.1:8080
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8

"""
