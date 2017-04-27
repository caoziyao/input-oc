
import threading
import socket
import json
import os
from time import ctime

HOST = ''
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)
DIR_PATH = os.path.abspath(os.curdir)
FILE_PATH = DIR_PATH + '\\user.txt'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

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

def valid_register():
	pass

def valid_login(id, passwd, item):
	return id == item.get('id', '') and passwd == item.get('password', '')

def load_from(path):
	with open(path, 'r', encoding='utf-8') as f:
		data = f.read()
		return json.loads(data)

def save(data, path):	
	data = json.dumps(data, indent=2, ensure_ascii=False)
	with open(path, 'w+', encoding='utf-8') as f:
		f.write(data)
		
def register(form):
	id = form.get('id', '')
	passwd = form.get('password', '')
	valid_register()
	
	info = {
		'id': id,
		'password': passwd
	}

	data = load_from(FILE_PATH)
	data.append(info)
	
	save(data, FILE_PATH)

	
def login(form):
	addr = form.get('addr', '')
	passwd = form.get('password', '')
				
	data = load_from(FILE_PATH)
	for item in data:
		if valid_login(addr, passwd, item):
			print('login success')
			return True
	return False
			
		#update_conn(src_ip, conn)			# 更新链接
		#handle_message(des_ip, data)		# 处理客户端发过的数据
	
	
def handle_login(conn, error):
	form = {
		'cmd': 'login',
		'err': error
	}
	s = json.dumps(form, ensure_ascii=False)
	s = s.encode('utf-8')
	conn.send(s)

def connection():
	while True:
		conn, addr = server.accept()
		print('connect from', addr)
		bbq = ServerBBQ(conn, addr)
		bbq.start()
	server.close()

# threading
class ServerBBQ(threading.Thread):
	def __init__(self, conn, addr):
		threading.Thread.__init__(self)
		self.conn = conn
		self.addr = addr
		self.isRunning = True

	def run(self):
		self.recv_message(self.conn, self.addr)

	def stop(self):
		self.isRunning = False
		
	def recv_message(self, conn, addr):
		while True:
			form = conn.recv(BUFSIZE)
			if not form:
				break
			form = form.decode('utf-8')
			
			form = json.loads(form)
			cmd = form.get('cmd', '')
			src_ip = form.get('src', '')
			des_ip = form.get('des', '')
			data = form.get('data', '')
			
			if data == 'kill':
				server.close()
				exit()
			
			print('client', form)
			
			if cmd == 'register':
				register(form)
			elif cmd == 'login':
				if login(form):
					handle_login(conn, True)
				else:
					handle_login(conn, False)

		
if __name__ == '__main__':
	connection()
		
	

#t1 = threading.Thread(target=recv_message, args=(conn, addr, ))
#t1.start()
# 	content = input('> ')
#	conn.send(content.encode('utf-8'))