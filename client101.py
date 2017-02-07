
import socket
import json
import threading

HOST = 'localhost'
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)
SRC = 101
DES = 100

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def recv_from():
	while True:
		fromseerver = client.recv(BUFSIZE)
		if not fromseerver:
			continue
		print('from ',DES, fromseerver)
	
t = threading.Thread(target=recv_from)
t.start()	
	
	
while True:
	data = input('> ')
	if data == 'q':
		break
	form = {
		'src': SRC,
		'des': DES,
		'data': data
	}
	s = json.dumps(form, ensure_ascii=False)
	s = s.encode('utf-8')
	client.send(s)



	
client.close()

"""
	fromseerver = client.recv(BUFSIZE)
	if not fromseerver:
		continue
	print('from server', fromseerver)
"""