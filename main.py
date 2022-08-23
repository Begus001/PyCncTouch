from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import os

from views.views import *
from grbl import *


class WinMain(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewMain = ViewMain()
		self.viewMain.setupUi(self)

		self.grbl = GrblInterface()
		self.grbl.connectionChanged.connect(self.grblConnectionChanged)

	def grblConnectionChanged(self, c):
		if not c:
			self.viewMain.pageJog.setEnabled(False)
		else:
			self.viewMain.pageJog.setEnabled(True)

	def connectPort(self):
		self.grbl.connectPort(self.viewMain.cbPorts.currentText())

	def switchPage(self):
		self.viewMain.stackMain.setCurrentIndex(QObject.sender(self).property("pageIndex"))

	def setFeed(self):
		self.diagFeed = DiagFeed()
		result = self.diagFeed.exec()
		self.viewMain.btFeed.setText(str(result))
		self.grbl.jogFeed = result

	def jogXNYP(self):
		self.grbl.jogXNYP()

	def jogYP(self):
		self.grbl.jogYP()

	def jogXPYP(self):
		self.grbl.jogXPYP()

	def jogXN(self):
		self.grbl.jogXN()

	def jogXP(self):
		self.grbl.jogXP()

	def jogXNYN(self):
		self.grbl.jogXNYN()

	def jogYN(self):
		self.grbl.jogYN()

	def jogXPYN(self):
		self.grbl.jogXPYN()

	def jogZP(self):
		self.grbl.jogZP()

	def jogZN(self):
		self.grbl.jogZN()

	def jogCancel(self):
		self.grbl.jogCancel()

	def fillDevices(self):
		self.viewMain.cbPorts.clear()
		for i in os.listdir("/dev"):
			if "ttyACM" in i:
				self.viewMain.cbPorts.addItem("/dev/" + i)

class DiagFeed(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewFeed = ViewFeed()
		self.viewFeed.setupUi(self)

	def returnFeed(self):
		feed = int(QObject.sender(self).text())
		self.done(feed)


app = QApplication()
m = WinMain()

for screen in app.screens():
	if screen.geometry().width() == 1024:
		m.move(screen.geometry().x(), screen.geometry().y())

m.show()
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
app.exec()
