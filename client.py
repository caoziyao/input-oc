
import socket
import json
import threading

HOST = 'localhost'
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)
ID = 0
DES_ID = 99
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(form):
	data = json.dumps(form, ensure_ascii=False)
	data = data.encode('utf-8')
	client.send(data)


class ClientBBQ():
	def __init__(self):
		print('starting BBQ, it make take few minutes...')
		cmd = input('register(r) / login(l)? ')
		self.handle_reg_or_login(cmd)
		self.id = 0
			
	def handle_reg_or_login(self, cmd):
		if cmd == 'r':
			self.register()
		elif cmd == 'l':
			self.login()
		else:
			print('please input r or l')
			#exit()
	
	def register(self):
		print('welcome to BBQ')
		self.id = input('id: ')
		self.id = int(self.id)
		bbq_passwd = input('password: ')
		form = {
			'cmd': 'register',
			'id': self.id,
			'password': bbq_passwd
		}
		send_message(form)

	def login(self):
		global ID
		ID = input('id: ')
		ID = int(ID)
		bbq_passwd = input('password: ')
		form = {
			'cmd': 'login',
			'addr': ID,
			'timeout': 0,
			'password': bbq_passwd
		}
		send_message(form)
		
	def chat(self):	
		while True:
			data = input('> ')
			if data == 'q':
				break
			form = {
				'src': self.id,
				'des': DES_ID,
				'data': data
			}
			s = json.dumps(form, ensure_ascii=False)
			s = s.encode('utf-8')
			client.send(s)
		client.close()	
	
def recv_from():
	while True:
		data = client.recv(BUFSIZE)
		if not data:
			continue
		
		data = data.decode('utf-8')
		data = json.loads(data)
		cmd = data.get('cmd', '')
		err = data.get('err', '')
		if cmd == 'login':
			if err:	
				bbq.id = ID
				print('from', bbq.id, data)
			else:
				print('login error')
			
		#print('from', bbq.id, data)
		
		
t = threading.Thread(target=recv_from)
t.setDaemon(True)
t.start()	
	


if __name__ == '__main__':
	bbq = ClientBBQ()
	bbq.chat()
	


"""
	fromseerver = client.recv(BUFSIZE)
	if not fromseerver:
		continue
	print('from server', fromseerver)
"""