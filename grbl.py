from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import serial as s
import time
import traceback
import os
import threading
import re

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

		self.shouldClose: bool = False
		self.stream: bool = False
		self.filepath: str = ""

		self.jogFeed: float = defaultFeed
		self.currentFeed: float = 0.0

		self.statusInterval = statusInterval

		self.state: str = "Idle"

		self.threadJog = threading.Thread(None, self.jogLoop)
		self.threadJog.start()

		self.threadStream = threading.Thread(None, self.streamLoop)
		self.threadStream.start()
		self.threadStreamStatus = threading.Thread(None, self.streamStatus)
		self.threadStreamStatus.start()

		self.mutexSerial = QMutex()


	def jogLoop(self) -> None:
		while not self.shouldClose:
			while self.stream: time.sleep(.5)

			time.sleep(self.statusInterval / 1000.0)
			if self.connected() and self.serial.isOpen():
				self.mutexSerial.lock()
				try:
					self.serial.write(b"?")

					while True:
						report = self.serial.readline().decode()
						if report.find("ok") >= 0 or report.find("error") >= 0: continue
						else: break

					curState = report[1:report.index("|")]
					if self.state != curState:
						self._setState(curState)

					self.statusUpdate.emit(GrblStatus(report))
				except:
					traceback.print_exc()
					self.serial.close()
					self._setConnected(False)
				finally:
					self.mutexSerial.unlock()


	def streamLoop(self) -> None:
		while not self.shouldClose:
			time.sleep(0.5)
			if self.stream:
				self.serial.reset_input_buffer()

				f = open(self.filepath, "r")
				
				lineIndex = 0
				sentIndex = 0
				charNum = []

				for line in f:
					lineIndex += 1
					lineStripped = re.sub('\s|\(.*?\)','',line).upper()

					charNum.append(len(lineStripped) + 1)

					while sum(charNum) >= 127 or self.serial.inWaiting():
						resp = self.serial.readline().strip().decode()
						print(resp)
						if "ok" not in resp and "error" not in resp:
							curState = resp[1:resp.index("|")]
							if self.state != curState:
								self._setState(curState)

							self.statusUpdate.emit(GrblStatus(resp))
						else:
							sentIndex += 1
							del charNum[0]
					
					self.serial.write(bytes(lineStripped, "utf-8") + b"\n")

				while lineIndex > sentIndex:
					while sum(charNum) >= 127 or self.serial.inWaiting():
						resp = self.serial.readline().strip().decode()
						print(resp)
						if "ok" not in resp and "error" not in resp:
							if resp == "[MSG:Pgm End]": break

							curState = resp[1:resp.index("|")]
							if self.state != curState:
								self._setState(curState)

							self.statusUpdate.emit(GrblStatus(resp))
						else:
							sentIndex += 1
							del charNum[0]
				
				self.stream = False


	def streamStatus(self):
		while not self.shouldClose:
			time.sleep(0.5)
			while self.stream:
				self.mutexSerial.lock()
				self.serial.write(b"?")
				self.mutexSerial.unlock()
				time.sleep(self.statusInterval / 1000.0)

	
	def _setConnected(self, c: bool) -> None:
		self._connected = c
		self.connectionChanged.emit(c)

	def connectPort(self, port: str) -> None:
		self.serial.port = port
		self.serial.baudrate = 115200
		try:
			self.serial.open()
			self.serial.write(b"\x18")
			self.serial.flush()
			print(self.serial.read_until(b"\r\n").decode())
			print(self.serial.read_all().decode())
			self._setConnected(True)
		except:
			self.serial.close()
			self._setConnected(False)

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
		if not self.connected(): return
		self.serial.write(b"\x85")

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

	def startNC(self, file: str) -> None:
		self.filepath = file
		self.stream = True


	def _sendCmd(self, cmd: bytes) -> None:
		if not self.connected(): return
		lock = QMutexLocker(self.mutexSerial)
		self.serial.write(cmd)
		self._waitOK()

	def _waitOK(self) -> bool:
		resp = self.serial.read_until(b"\r\n")
		if resp != b"ok\r\n":
			print("RESP: " + repr(resp))
			return False
		return True
