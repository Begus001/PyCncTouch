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
		self.z: float = float(report[:report.index("|")])
		report = report[report.index("|")+4:]
		self.currentFeed: float = float(report[:report.index(",")])


class GrblInterface(QObject):
	connectionChanged = Signal(bool)
	statusUpdate = Signal(GrblStatus)
	stateChanged = Signal(str)

	def __init__(self, defaultFeed: float, statusInterval: int):
		super().__init__()
		self._connected: bool = False
		self.serial = s.Serial()

		self.jogFeed: float = defaultFeed
		self.currentFeed: float = 0.0

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
		self._sendCmd(b"$J=F%f G91 X-1000 Y1000\n" % (self.jogFeed))

	def jogYP(self) -> None:
		self._sendCmd(b"$J=F%f G91 Y1000\n" % (self.jogFeed))

	def jogXPYP(self) -> None:
		self._sendCmd(b"$J=F%f G91 X1000 Y1000\n" % (self.jogFeed))

	def jogXN(self) -> None:
		self._sendCmd(b"$J=F%f G91 X-1000\n" % (self.jogFeed))

	def jogXP(self) -> None:
		self._sendCmd(b"$J=F%f G91 X1000\n" % (self.jogFeed))

	def jogXNYN(self) -> None:
		self._sendCmd(b"$J=F%f G91 X-1000 Y-1000\n" % (self.jogFeed))

	def jogYN(self) -> None:
		self._sendCmd(b"$J=F%f G91 Y-1000\n" % (self.jogFeed))

	def jogXPYN(self) -> None:
		self._sendCmd(b"$J=F%f G91 X1000 Y-1000\n" % (self.jogFeed))
	
	def jogZP(self) -> None:
		self._sendCmd(b"$J=F%f G91 Z1000\n" % (self.jogFeed))
	
	def jogZN(self) -> None:
		self._sendCmd(b"$J=F%f G91 Z-1000\n" % (self.jogFeed))

	def jogCancel(self) -> None:
		self.serial.write(b"\x85")
		self.serial.flush()

	def gotoZeroX(self) -> None:
		self._sendCmd(b"G0 X0\n")

	def gotoZeroY(self) -> None:
		self._sendCmd(b"G0 Y0\n")

	def gotoZeroZ(self) -> None:
		self._sendCmd(b"G0 Z0\n")

	def zeroWorkX(self) -> None:
		self._sendCmd(b"G10 L20 P0 X0\n")

	def zeroWorkY(self) -> None:
		self._sendCmd(b"G10 L20 P0 Y0\n")

	def zeroWorkZ(self) -> None:
		self._sendCmd(b"G10 L20 P0 Z0\n")

	def _sendCmd(self, cmd: bytes) -> None:
		self.serial.read_all()
		self.serial.write(cmd)
		self._waitOK()

	def _waitOK(self) -> bool:
		resp = self.serial.read_until(b"\r\n")
		if resp != b"ok\r\n":
			print("RESP: " + repr(resp))
			return False
		return True
