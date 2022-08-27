from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import os

from views.views import *
from grbl import *


GRBL_UPDATE_INTERVAL_MS = 100
DEFAULT_FEED = 5000.0
NC_DIR = "/home/main/sync/cnc"


class WinMain(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewMain = ViewMain()
		self.viewMain.setupUi(self)

		self.grbl = GrblInterface(DEFAULT_FEED, GRBL_UPDATE_INTERVAL_MS)
		self.grbl.connectionChanged.connect(self.grblConnectionChanged)
		self.grbl.statusUpdate.connect(self.grblStatusUpdate)
		self.grbl.stateChanged.connect(self.grblStateChanged)

	def grblConnectionChanged(self, c: bool) -> None:
		if not c:
			self.viewMain.pageJog.setEnabled(False)
			self.viewMain.pageNC.setEnabled(False)
			self.viewMain.pageConnect.setEnabled(True)
			self.viewMain.lbConnected.setText("Disconnected")
			self.viewMain.cbPorts.clear()
		else:
			self.viewMain.pageJog.setEnabled(True)
			self.viewMain.pageNC.setEnabled(True)
			self.viewMain.pageConnect.setEnabled(False)
			self.viewMain.lbConnected.setText("Connected")

	def grblStatusUpdate(self, s: GrblStatus) -> None:
		self.viewMain.btZeroX.setText("%.3f" % (s.x))
		self.viewMain.btZeroY.setText("%.3f" % (s.y))
		self.viewMain.btZeroZ.setText("%.3f" % (s.z))
		self.viewMain.lbCurrentFeed.setText("%.0f" % (s.currentFeed))

	def grblStateChanged(self, s: str) -> None:
		self.viewMain.lbState.setText(s)

	def connectPort(self) -> None:
		self.grbl.connectPort(self.viewMain.cbPorts.currentText())

	def switchPage(self) -> None:
		self.viewMain.stackMain.setCurrentIndex(QObject.sender(self).property("pageIndex"))

	def setFeed(self) -> None:
		self.diagFeed = DiagFeed()
		result = self.diagFeed.exec()
		self.viewMain.btFeed.setText(str(result))
		self.grbl.jogFeed = result

	def jogXNYP(self) -> None:
		self.grbl.jogXNYP()

	def jogYP(self) -> None:
		self.grbl.jogYP()

	def jogXPYP(self) -> None:
		self.grbl.jogXPYP()

	def jogXN(self) -> None:
		self.grbl.jogXN()

	def jogXP(self) -> None:
		self.grbl.jogXP()

	def jogXNYN(self) -> None:
		self.grbl.jogXNYN()

	def jogYN(self) -> None:
		self.grbl.jogYN()

	def jogXPYN(self) -> None:
		self.grbl.jogXPYN()

	def jogZP(self) -> None:
		self.grbl.jogZP()

	def jogZN(self) -> None:
		self.grbl.jogZN()

	def jogCancel(self) -> None:
		self.grbl.jogCancel()

	def gotoZeroX(self) -> None:
		self.grbl.gotoZeroX()

	def gotoZeroY(self) -> None:
		self.grbl.gotoZeroY()

	def gotoZeroZ(self) -> None:
		self.grbl.gotoZeroZ()

	def zeroWorkX(self) -> None:
		self.grbl.zeroWorkX()

	def zeroWorkY(self) -> None:
		self.grbl.zeroWorkY()

	def zeroWorkZ(self) -> None:
		self.grbl.zeroWorkZ()

	def fillDevices(self) -> None:
		self.viewMain.cbPorts.clear()
		for i in os.listdir("/dev"):
			if "ttyUSB" in i or "ttyACM" in i:
				self.viewMain.cbPorts.addItem("/dev/" + i)

	def openNC(self):
		self.diagOpen = DiagOpen()
		ret = self.diagOpen.exec()
		if ret:
			self.grbl.filepath = os.path.join(NC_DIR, self.diagOpen.selectedFile)
		else:
			print("cancel")

	def startNC(self):
		self.grbl.stream = True

	def unlock(self):
		self.grbl.unlock()


class DiagFeed(QDialog):
	def __init__(self) -> None:
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewFeed = ViewFeed()
		self.viewFeed.setupUi(self)

	def returnFeed(self) -> None:
		feed = int(QObject.sender(self).text())
		self.done(feed)


class DiagOpen(QDialog):
	def __init__(self) -> None:
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewOpen = ViewOpen()
		self.viewOpen.setupUi(self)
		self.selectedFile: str

		for name in os.listdir(NC_DIR):
			if os.path.isdir(os.path.join(NC_DIR, name)):
				item = QListWidgetItem(QIcon.fromTheme("folder"), name)
			else:
				item = QListWidgetItem(QIcon.fromTheme("document"), name)
			item.setSizeHint(QSize(0, 60))
			item.setFont(QFont(self.font().family(), 20))
			self.viewOpen.listFiles.addItem(item)

	def returnFile(self) -> None:
		self.selectedFile = os.path.join(NC_DIR, self.viewOpen.listFiles.selectedItems()[0].text())
		self.done(1)

	def cancel(self) -> None:
		self.done(0)


app = QApplication()
m = WinMain()

# for screen in app.screens():
# 	if screen.geometry().width() == 1024:
# 		m.move(screen.geometry().x(), screen.geometry().y())

m.show()
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
app.exec()
m.grbl.shouldClose = True
