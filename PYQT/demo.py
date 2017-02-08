


from PyQt5 import QtWidgets, QtCore
from first import firstwindows


def mainwindows():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	windows = firstwindows()
	windows.resize(400, 100)
	windows.show()
	exit(app.exec_())
		
		
if __name__ == '__main__':
	mainwindows()
