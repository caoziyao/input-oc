
import sys

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
		

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


	
	
#client.close()
	

class Dialog(QDialog):
	""" BBQ Dialog
	"""
	def __init__(self, parent=None):
		super(Dialog, self).__init__(parent)
		
		self.bigEditor = QTextEdit()
		self.chatEditor = QTextEdit()
		
		self.button = QPushButton('send')
		self.button.clicked.connect(self.messageSend)
		
		hLayout = QHBoxLayout()
		hLayout.addWidget(self.chatEditor)
		hLayout.addWidget(self.button)
		
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.bigEditor)
		mainLayout.addLayout(hLayout)
		
		self.setLayout(mainLayout)
		
		self.setWindowTitle('BBQ')
		
	def messageSend(self):
		data = self.chatEditor.toPlainText()
		#print('send!!', data)
		if data == 'q':
			client.close()
		form = {
			'src': SRC,
			'des': DES,
			'data': data
		}
		s = json.dumps(form, ensure_ascii=False)
		s = s.encode('utf-8')
		client.send(s)

app = QApplication(sys.argv)		
dialog = Dialog()

def recv_from():
	while True:
		fromseerver = client.recv(BUFSIZE)
		if not fromseerver:
			continue
		print('from', DES, fromseerver)
		dialog.bigEditor.setText(fromseerver.decode('utf-8'))
	
t = threading.Thread(target=recv_from)
t.start()			
		
if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())