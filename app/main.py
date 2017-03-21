# coding: utf-8

import socket
from util import log


port = 8081
host = ''   # '' 代表接收任意 ip

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
def parsed_request(request):
    method = request.split()
    headers = request.split('\r\n\r\n', 1)[0].split('\r\n')[1:]
    body = request.split('\r\n\r\n', 1)[1]

    log(headers)

def run(host='', port=3000, debug=False):
    log('runing server...')
    s = Server(host, port)

    try:
        while True:
            # 接收一个连接
            connection, addr = s.accept()
            data = connection.recv(1024)
            data = data.decode('utf-8')
            parsed_request(data)
    except Exception as e:
        log('error main', e)
        s.close()

if __name__ == '__main__':
    config = dict(
        host= '',
        port= 3000,
        debug = True,
    )
    run(**config)


