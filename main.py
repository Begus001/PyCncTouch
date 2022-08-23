from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from views.views import *


class WinMain(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewMain = ViewMain()
		self.viewMain.setupUi(self)

	def switchPage(self):
		self.viewMain.stackMain.setCurrentIndex(QObject.sender(self).property("pageIndex"))

	def setFeed(self):
		self.diagFeed = DiagFeed()
		result = self.diagFeed.exec()
		self.viewMain.btFeed.setText(str(result))

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