from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import serial as s
import time


class GrblStatus:
	def __init__(self, report: str):
		report = report[report.index("|")+6:]
		self.x: float = float(report[:report.index(",")])
		report = report[report.index(",")+1:]
		self.y: float = float(report[:report.index(",")])
		report = report[report.index(",")+1:]
		self.z: float = float(report[:report.index(",")])


class GrblInterface(QObject):
	connectionChanged = Signal(bool)
	statusUpdate = Signal(GrblStatus)
	stateChanged = Signal(str)

	def __init__(self, defaultFeed: float, statusInterval: int):
		super().__init__()
		self._connected: bool = False
		self.serial = s.Serial()

		self.jogFeed: float = defaultFeed

		self.state: str = "Idle"

		self.timerStatus = QTimer()
		self.timerStatus.setInterval(statusInterval)
		self.timerStatus.timeout.connect(self.getStatus)
		self.timerStatus.start()

	def getStatus(self) -> None:
		if self.connected() and self.serial.isOpen():
			try:
				self.serial.write(b"?")
				c = self.serial.read(1)
				if c != b"<": return

				report = self.serial.read_until(b"\r\n").decode()

				curState = report[0:report.index("|")]
				if self.state != curState:
					self._setState(curState)

				self.statusUpdate.emit(GrblStatus(report))
			except:
				self.serial.close()
				self._setConnected(False)
	
	def _setConnected(self, c: bool) -> None:
		self._connected = c
		self.connectionChanged.emit(c)

	def connectPort(self, port: str) -> None:
		self.serial.port = port
		self.serial.baudrate = 115200
		self.serial.timeout = 1
		self.serial.open()
		self.serial.write(b"\r\n\r\n")
		time.sleep(2)
		self.serial.flushInput()
		self._setConnected(True)

	def connected(self) -> bool:
		return self._connected

	def _setState(self, s: str) -> None:
		self.state = s
		self.stateChanged.emit(s)

	def jogXNYP(self) -> None:
		self.serial.write(b"$J=F%f G91 X-1000 Y1000\n" % (self.jogFeed))
		self._waitOK()

	def jogYP(self) -> None:
		self.serial.write(b"$J=F%f G91 Y1000\n" % (self.jogFeed))
		self._waitOK()

	def jogXPYP(self) -> None:
		self.serial.write(b"$J=F%f G91 X1000 Y1000\n" % (self.jogFeed))
		self._waitOK()

	def jogXN(self) -> None:
		self.serial.write(b"$J=F%f G91 X-1000\n" % (self.jogFeed))
		self._waitOK()

	def jogXP(self) -> None:
		self.serial.write(b"$J=F%f G91 X1000\n" % (self.jogFeed))
		self._waitOK()

	def jogXNYN(self) -> None:
		self.serial.write(b"$J=F%f G91 X-1000 Y-1000\n" % (self.jogFeed))
		self._waitOK()

	def jogYN(self) -> None:
		self.serial.write(b"$J=F%f G91 Y-1000\n" % (self.jogFeed))
		self._waitOK()

	def jogXPYN(self) -> None:
		self.serial.write(b"$J=F%f G91 X1000 Y-1000\n" % (self.jogFeed))
		self._waitOK()
	
	def jogZP(self) -> None:
		self.serial.write(b"$J=F%f G91 Z1000\n" % (self.jogFeed))
		self._waitOK()
	
	def jogZN(self) -> None:
		self.serial.write(b"$J=F%f G91 Z-1000\n" % (self.jogFeed))
		self._waitOK()

	def jogCancel(self) -> None:
		self.serial.write(b"\x85")
		self.serial.flush()

	def gotoZeroX(self) -> None:
		self.serial.write(b"G0 X0\n")
		self._waitOK()

	def gotoZeroY(self) -> None:
		self.serial.write(b"G0 Y0\n")
		self._waitOK()

	def gotoZeroZ(self) -> None:
		self.serial.write(b"G0 Z0\n")
		self._waitOK()

	def _waitOK(self) -> None:
		resp = self.serial.read_until(b"\r\n")
		# if resp == b"ok\r\n":
		# 	print("OK")
		# else:
		# 	print("NOTOK " + repr(resp))
