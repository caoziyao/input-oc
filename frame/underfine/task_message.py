

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