from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import serial as s
import time


class GrblInterface(QObject):
	connectionChanged = Signal(bool)
	def __init__(self):
		super().__init__()
		self._connected: bool = False
		self.serial: s.Serial = s.Serial()

		self.jogFeed: float = 5000.0
	
	def _setConnected(self, c: bool) -> None:
		self._connected = c
		self.connectionChanged.emit(c)

	def connectPort(self, port: str) -> None:
		self.serial.port = port
		self.serial.baudrate = 115200
		self.serial.open()
		self.serial.write(b"\r\n\r\n")
		time.sleep(2)
		print(self.serial.read_all().decode())
		self._setConnected(True)

	def connected(self) -> bool:
		return self._connected

	def jogXNYP(self):
		self.serial.write(b"$J=F%f G91 X-1000 Y1000\n" % (self.jogFeed))

	def jogYP(self):
		self.serial.write(b"$J=F%f G91 Y1000\n" % (self.jogFeed))

	def jogXPYP(self):
		self.serial.write(b"$J=F%f G91 X1000 Y1000\n" % (self.jogFeed))

	def jogXN(self):
		self.serial.write(b"$J=F%f G91 X-1000\n" % (self.jogFeed))

	def jogXP(self):
		self.serial.write(b"$J=F%f G91 X1000\n" % (self.jogFeed))

	def jogXNYN(self):
		self.serial.write(b"$J=F%f G91 X-1000 Y-1000\n" % (self.jogFeed))

	def jogYN(self):
		self.serial.write(b"$J=F%f G91 Y-1000\n" % (self.jogFeed))

	def jogXPYN(self):
		self.serial.write(b"$J=F%f G91 X1000 Y-1000\n" % (self.jogFeed))
	
	def jogZP(self):
		self.serial.write(b"$J=F%f G91 Z1000\n" % (self.jogFeed))
	
	def jogZN(self):
		self.serial.write(b"$J=F%f G91 Z-1000\n" % (self.jogFeed))

	def jogCancel(self):
		self.serial.write(b"\x85")
