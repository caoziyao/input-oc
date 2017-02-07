
import threading
import socket
import json
from time import ctime

HOST = ''
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

"""
	form = {
		'src': SRC,
		'des': DES,
		'data': data
	}
"""
connections = [{'ip': 0, 'conn': ''}]

def update_conn(src, conn):
	c = {
		'ip': src,
		'conn': conn
	}
	for l in connections:
		if src == l.get('ip'):
			return
	connections.append(c)
	
def handle_message(des_ip, data):
	"""处理客户端发过的数据
	"""
	for c in connections:
		if des_ip == c.get('ip'):
			des_conn = c.get('conn')
			des_conn.send(data.encode('utf-8'))

def recv_from(conn, addr):
	while True:
		form = conn.recv(BUFSIZE)
		if not form:
			break
		form = form.decode('utf-8')
		
		form = json.loads(form, encoding='utf-8')
		src_ip = form.get('src', '')
		des_ip = form.get('des', '')
		data = form.get('data', '')
		
		print('client', form)
		update_conn(src_ip, conn)			# 更新链接
		handle_message(des_ip, data)		# 处理客户端发过的数据
	


def connection():
	conn, addr = server.accept()
	print('connect from', addr)


if __name__ == '__main__':
	while True:
		conn, addr = server.accept()
		print('connect from', addr)
		t1 = threading.Thread(target=recv_from, args=(conn, addr, ))
		t1.start()
		
	server.close()


# 	content = input('> ')
#	conn.send(content.encode('utf-8'))