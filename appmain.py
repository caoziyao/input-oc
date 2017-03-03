

import socket
import json
import threading
from clientbbq import ClientBBQ
from task_message import recv_from

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