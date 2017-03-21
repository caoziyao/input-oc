
import socket
from util import log


port = 8081
host = ''
# tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    # 接收一个连接
    connection, addr = s.accept()
    data = connection.recv(1024)
    data = data.decode('utf-8')
    log('data', data)
