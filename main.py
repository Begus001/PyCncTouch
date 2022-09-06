from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import os

from views.views import *
from grbl import *


GRBL_UPDATE_INTERVAL_MS = 100
DEFAULT_FEED = 5000
DEFAULT_INCDIST = 0.01
NC_DIR = "/home/main/sync/cnc/"


class WinMain(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewMain = ViewMain()
		self.viewMain.setupUi(self)
		self.grblConnectionChanged(False)

		with open("style.qss") as f:
			self.style = f.read()

		self.setStyleSheet(self.style)

		self.grbl = GrblInterface(DEFAULT_FEED, DEFAULT_INCDIST, GRBL_UPDATE_INTERVAL_MS)
		self.grbl.connectionChanged.connect(self.grblConnectionChanged)
		self.grbl.statusUpdate.connect(self.grblStatusUpdate)
		self.grbl.stateChanged.connect(self.grblStateChanged)
		self.grbl.processedIndexChanged.connect(self.selectGcodeLine)
		self.grbl.streamStatusChanged.connect(self.grblStreamStatusChanged)

		self.destroyed.connect(self.closeGrblThreads)

		self.jogMode: bool = True
		self.jogFeed: int = DEFAULT_FEED
		self.incDist: float = DEFAULT_INCDIST

		self.gcode: str

		self.fillDevices()

	def closeGrblThreads(self):
		self.grbl.shouldClose = True

	def selectGcodeLine(self, i) -> None:
		self.viewMain.listGcode.setCurrentRow(i)
		self.viewMain.gcodeViewer.gcodeIndex = i

	def grblStreamStatusChanged(self, stream: bool) -> None:
		if stream:
			self.viewMain.pageJog.setEnabled(False)
			self.viewMain.btStart.setEnabled(False)
			self.viewMain.btOpen.setEnabled(False)
			self.viewMain.btUnlock.setEnabled(False)
		else:
			if self.grbl.connected:
				self.viewMain.pageJog.setEnabled(True)
				self.viewMain.btStart.setEnabled(True)
				self.viewMain.btUnlock.setEnabled(True)
			self.viewMain.btOpen.setEnabled(True)
			self.viewMain.listGcode.setCurrentRow(0)
			self.viewMain.listGcode.setCurrentRow(-1)

	def grblConnectionChanged(self, c: bool) -> None:
		if not c:
			self.viewMain.pageJog.setEnabled(False)
			self.viewMain.cbPorts.setEnabled(True)
			self.viewMain.btConnect.setText("Connect")
			self.viewMain.lbConnected.setText("Disconnected")
			self.viewMain.btStart.setEnabled(False)
			self.viewMain.btUnlock.setEnabled(False)
		else:
			self.viewMain.pageJog.setEnabled(True)
			self.viewMain.cbPorts.setEnabled(False)
			self.viewMain.btConnect.setText("Disconnect")
			self.viewMain.lbConnected.setText("Connected")
			self.viewMain.btStart.setEnabled(True)
			self.viewMain.btUnlock.setEnabled(True)

	def grblStatusUpdate(self, s: GrblStatus) -> None:
		self.viewMain.btSetX.setText("%.3f" % (s.x))
		self.viewMain.btSetY.setText("%.3f" % (s.y))
		self.viewMain.btSetZ.setText("%.3f" % (s.z))
		self.viewMain.lbX.setText("X%.3f" % (s.x))
		self.viewMain.lbY.setText("Y%.3f" % (s.y))
		self.viewMain.lbZ.setText("Z%.3f" % (s.z))
		self.viewMain.lbF.setText("F%.1f" % (s.currentFeed))
		self.viewMain.lbS.setText("S%.0f" % (s.currentSpeed))
		self.viewMain.gcodeViewer.curx = s.x
		self.viewMain.gcodeViewer.cury = s.y
		self.viewMain.gcodeViewer.update()

	def grblStateChanged(self, s: str) -> None:
		self.viewMain.lbState.setText(s)
		if "Alarm" in s:
			self.viewMain.pageJog.setEnabled(False)
			self.viewMain.btStart.setEnabled(False)
		else:
			if not self.grbl.stream:
				self.viewMain.pageJog.setEnabled(True)
				self.viewMain.btStart.setEnabled(True)

	def connectPort(self) -> None:
		if not self.grbl.connected:
			self.grbl.connectPort(self.viewMain.cbPorts.currentText())
		else:
			self.grbl.setConnected(False)

	def switchPage(self) -> None:
		self.viewMain.stackMain.setCurrentIndex(QObject.sender(self).property("pageIndex"))

	def setFeed(self) -> None:
		if self.jogMode:
			diagFeed = DiagFeed(self.style)
			self.jogFeed = diagFeed.exec()
			self.viewMain.btFeed.setText(str(self.jogFeed))
			self.grbl.jogFeed = self.jogFeed
		else:
			diagDistance = DiagDistance(self.style)
			diagDistance.exec()
			self.incDist = diagDistance.selectedDistance
			self.viewMain.btFeed.setText(str(self.incDist))
			self.grbl.incDist = self.incDist

	def jogXNYP(self) -> None:
		if self.jogMode:
			self.grbl.jogXNYP()
		else:
			self.grbl.moveXNYP()

	def jogYP(self) -> None:
		if self.jogMode:
			self.grbl.jogYP()
		else:
			self.grbl.moveYP()

	def jogXPYP(self) -> None:
		if self.jogMode:
			self.grbl.jogXPYP()
		else:
			self.grbl.moveXPYP()

	def jogXN(self) -> None:
		if self.jogMode:
			self.grbl.jogXN()
		else:
			self.grbl.moveXN()

	def jogXP(self) -> None:
		if self.jogMode:
			self.grbl.jogXP()
		else:
			self.grbl.moveXP()

	def jogXNYN(self) -> None:
		if self.jogMode:
			self.grbl.jogXNYN()
		else:
			self.grbl.moveXNYN()

	def jogYN(self) -> None:
		if self.jogMode:
			self.grbl.jogYN()
		else:
			self.grbl.moveYN()

	def jogXPYN(self) -> None:
		if self.jogMode:
			self.grbl.jogXPYN()
		else:
			self.grbl.moveXPYN()

	def jogZP(self) -> None:
		if self.jogMode:
			self.grbl.jogZP()
		else:
			self.grbl.moveZP()

	def jogZN(self) -> None:
		if self.jogMode:
			self.grbl.jogZN()
		else:
			self.grbl.moveZN()

	def jogCancel(self) -> None:
		self.grbl.jogCancel()

	def gotoZeroX(self) -> None:
		self.grbl.gotoZeroX()

	def gotoZeroY(self) -> None:
		self.grbl.gotoZeroY()

	def gotoZeroZ(self) -> None:
		self.grbl.gotoZeroZ()

	def switchJogMode(self) -> None:
		self.jogMode = not self.jogMode
		if self.jogMode:
			self.viewMain.btFeed.setText(str(self.jogFeed))
			self.viewMain.btJogMode.setText("Feed")
		else:
			self.viewMain.btFeed.setText(str(self.incDist))
			self.viewMain.btJogMode.setText("Distance")

	def setWorkX(self) -> None:
		diag = DiagSetAxis(float(self.viewMain.btSetX.text()))
		if diag.exec():
			self.grbl.setX(diag.enteredValue)

	def setWorkY(self) -> None:
		diag = DiagSetAxis(float(self.viewMain.btSetY.text()))
		if diag.exec():
			self.grbl.setY(diag.enteredValue)

	def setWorkZ(self) -> None:
		diag = DiagSetAxis(float(self.viewMain.btSetZ.text()))
		if diag.exec():
			self.grbl.setZ(diag.enteredValue)

	def fillDevices(self) -> None:
		self.viewMain.cbPorts.clear()
		for i in os.listdir("/dev"):
			if "ttyUSB" in i or "ttyACM" in i:
				self.viewMain.cbPorts.addItem("/dev/" + i)

	def openNC(self):
		self.diagOpen = DiagOpen(self.style)
		ret = self.diagOpen.exec()
		if ret:
			with open(self.diagOpen.selectedFile, "r") as f:
				self.gcode = ""
				for line in f:
					l = re.sub("\s|\(.*?\)", "", line)
					if l != "":
						self.gcode += l + "\n"
				self.grbl.loadNC(self.gcode)
				self.viewMain.listGcode.clear()
				self.viewMain.listGcode.addItems(self.gcode.splitlines())
				self.viewMain.gcodeViewer.loadGcode(self.gcode)

	def startNC(self):
		self.grbl.startNC()

	def unlock(self):
		self.grbl.unlock()

	def zoomIn(self):
		self.viewMain.gcodeViewer.zoomIn()

	def zoomOut(self):
		self.viewMain.gcodeViewer.zoomOut()
	
	def zoomToFit(self):
		self.viewMain.gcodeViewer.analyzeLimits()


class DiagFeed(QDialog):
	def __init__(self, style: str) -> None:
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewFeed = ViewFeed()
		self.viewFeed.setupUi(self)
		self.setStyleSheet(style)

	def returnFeed(self) -> None:
		feed = int(QObject.sender(self).text())
		self.done(feed)


class DiagDistance(QDialog):
	def __init__(self, style: str) -> None:
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewDistance = ViewDistance()
		self.viewDistance.setupUi(self)

		self.setStyleSheet(style)

		self.selectedDistance: float

	def returnDistance(self) -> None:
		distance = float(QObject.sender(self).text())
		self.selectedDistance = distance
		self.close()


class DiagOpen(QDialog):
	def __init__(self, style: str) -> None:
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewOpen = ViewOpen()
		self.viewOpen.setupUi(self)

		self.setStyleSheet(style)

		self.currentDir: str = NC_DIR
		self.selectedFile: str

		self.scrollbar = QScrollBar(Qt.Orientation.Vertical, self.viewOpen.listFiles)
		self.scrollbar.setStyleSheet("QScrollBar:vertical{width:100px;}")
		self.viewOpen.listFiles.setVerticalScrollBar(self.scrollbar)
		self.viewOpen.listFiles.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

		self.listdir()

	def listdir(self) -> None:
		self.viewOpen.listFiles.clear()

		if self.currentDir != "/":
			item = QListWidgetItem(QIcon.fromTheme("folder"), "..")
			item.setSizeHint(QSize(0, 60))
			item.setFont(QFont(self.font().family(), 20))
			self.viewOpen.listFiles.addItem(item)

		for name in sorted(os.listdir(self.currentDir)):
			if os.path.isdir(os.path.join(self.currentDir, name)):
				item = QListWidgetItem(QIcon.fromTheme("folder"), name)
			else:
				item = QListWidgetItem(QIcon.fromTheme("document"), name)
			item.setSizeHint(QSize(0, 60))
			item.setFont(QFont(self.font().family(), 20))
			self.viewOpen.listFiles.addItem(item)
		self.viewOpen.listFiles.setCurrentRow(0)

	def returnFile(self) -> None:
		sel = self.viewOpen.listFiles.selectedItems()[0].text()
		path = os.path.join(self.currentDir, sel)
		if sel == "..":
			self.currentDir = self.currentDir[:self.currentDir[:-1].rindex("/")+1]
			self.listdir()
		elif os.path.isdir(path):
			self.currentDir = path
			self.listdir()
		else:
			self.selectedFile = path
			self.done(1)

	def cancel(self) -> None:
		self.done(0)


class DiagSetAxis(QDialog):
	def __init__(self, currentValue: float):
		super().__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.viewSetAxis = ViewSetAxis()
		self.viewSetAxis.setupUi(self)

		self.currentValue: float = currentValue

		self.enteredValue: float
	
	def keypadEntry(self) -> None:
		val = QObject.sender(self).text()
		current = self.viewSetAxis.lbValue.text()
		if val == "Backspace":
			if len(current) > 0:
				self.viewSetAxis.lbValue.setText(current[:-1])
		elif val == ".":
			if "." not in current and len(current) < 9:
				self.viewSetAxis.lbValue.setText(current + val)
		else:
			if len(current) < 10:
				self.viewSetAxis.lbValue.setText(current + val)
		
	def returnValue(self) -> None:
		val = self.viewSetAxis.lbValue.text()
		self.enteredValue = float(val)
		self.done(1)
		
	def returnValueNegative(self) -> None:
		val = self.viewSetAxis.lbValue.text()
		self.enteredValue = float(val)
		self.enteredValue = -float(val)
		self.done(1)

	def cancel(self) -> None:
		self.done(0)
		
	def returnZero(self) -> None:
		self.enteredValue = 0.0
		self.done(1)
		
	def returnHalf(self) -> None:
		self.enteredValue = self.currentValue / 2
		self.done(1)


app = QApplication()
m = WinMain()

for screen in app.screens():
	if screen.geometry().width() == 1024:
		m.move(screen.geometry().x(), screen.geometry().y())

m.show()
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
app.exec()
m.grbl.shouldClose = True
m.viewMain.gcodeViewer.shouldClose = True
