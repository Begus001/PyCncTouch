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
		self.connected: bool = False
		self.serial = s.Serial()

		self.shouldClose: bool = False
		self.stream: bool = False
		self.filepath: str = ""

		self.jogFeed: float = defaultFeed
		self.currentFeed: float = 0.0

		self.statusInterval = statusInterval

		self.state: str = "Idle"

		self.threadReceiver = threading.Thread(target=self.receiverLoop, name="receiver")
		self.threadReceiver.start()

		self.threadStatus = threading.Thread(target=self.statusLoop, name="status")
		self.threadStatus.start()

		self.threadConnection = threading.Thread(target=self.connectionKeepAlive, name="connection")
		self.threadConnection.start()

		self.mutexSerial = QMutex()

		self.keepAlive: bool = True

		self.bytesInBuf: list[int] = []


	def receiverLoop(self) -> None:
		while not self.shouldClose:
			if self.connected:
				if not self.stream:
					if self.serial.inWaiting():
						resp = self.serial.readline().decode().strip()
						if "ok" in resp or "error" in resp:
							del self.bytesInBuf[0]
						elif resp.startswith("<"):
							self.keepAlive = True
							self.state = resp[1:resp.index("|")]
							self.stateChanged.emit(self.state)
							self.statusUpdate.emit(GrblStatus(resp))
				else:
					f = open(self.filepath, "r")
					lineIndex = 0
					processedIndex = 0

					for line in f:
						lineIndex += 1
						l = re.sub("\s|\(.*?\)", "", line) + "\n"
						self.bytesInBuf.append(len(l))

						while sum(self.bytesInBuf) > 127 or self.serial.inWaiting() and self.stream and self.connected:
							if "Alarm" in self.state or not self.connected or not self.serial.isOpen():
								self.stream = False
								break
							
							if self.connected and self.serial.isOpen() and self.stream:
								resp = self.serial.readline().decode().strip()
							else: break

							if "ok" in resp or "error" in resp:
								processedIndex += 1
								del self.bytesInBuf[0]
							elif "<" in resp:
								self.keepAlive = True
								self.state = resp[1:resp.index("|")]
								self.stateChanged.emit(self.state)
								self.statusUpdate.emit(GrblStatus(resp))

							if "Alarm" in self.state or not self.connected or not self.serial.isOpen():
								self.stream = False
								break

						if "Alarm" in self.state or not self.connected or not self.serial.isOpen():
								self.stream = False
								break

						print(l.strip())
						if self.connected and self.stream and self.serial.isOpen():
							self.serial.write(bytes(l, "utf-8"))
						else:
							self.stream = False
					
					while processedIndex < lineIndex and self.stream and self.connected and self.serial.isOpen():
						while not self.serial.inWaiting():
							if not self.connected:
								self.stream = False
						if not self.stream: break
						resp = self.serial.readline().decode().strip()
						if "ok" in resp or "error" in resp:
								processedIndex += 1
								del self.bytesInBuf[0]
						elif "<" in resp:
							self.keepAlive = True
							self.state = resp[1:resp.index("|")]
							self.stateChanged.emit(self.state)
							self.statusUpdate.emit(GrblStatus(resp))
					
					self.stream = False
					self.bytesInBuf.clear()
					if self.serial.isOpen():
						self.serial.read_all()

					f.close()
						

				time.sleep(0.001)
			else:
				time.sleep(0.5)


	def statusLoop(self):
		while not self.shouldClose:
			time.sleep(0.5)
			while self.connected and self.serial.isOpen():
				self.mutexSerial.lock()
				self.serial.write(b"?")
				self.mutexSerial.unlock()
				time.sleep(self.statusInterval / 1000.0)

	def connectionKeepAlive(self):
		while not self.shouldClose:
			time.sleep(.5)
			if not self.keepAlive and self.connected:
				self.setConnected(False)
			self.keepAlive = False

	def setConnected(self, c: bool) -> None:
		self.connected = c
		self.connectionChanged.emit(c)
		if c:
			self.serial.reset_input_buffer()
			self.keepAlive = True
		if not c and self.serial.isOpen():
			time.sleep(.2)
			self.serial.close()

	def connectPort(self, port: str) -> None:
		self.serial.port = port
		self.serial.baudrate = 115200
		try:
			self.serial.open()
			self.serial.write(b"\x18")
			self.serial.flush()
			print(self.serial.read_until(b"\r\n").decode())
			print(self.serial.read_all().decode())
			self.setConnected(True)
		except:
			self.setConnected(False)

	def _setState(self, s: str) -> None:
		self.state = s
		self.stateChanged.emit(s)

	def jogXNYP(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 X-1000 Y1000\n" % (self.jogFeed))

	def jogYP(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 Y1000\n" % (self.jogFeed))

	def jogXPYP(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 X1000 Y1000\n" % (self.jogFeed))

	def jogXN(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 X-1000\n" % (self.jogFeed))

	def jogXP(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 X1000\n" % (self.jogFeed))

	def jogXNYN(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 X-1000 Y-1000\n" % (self.jogFeed))

	def jogYN(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 Y-1000\n" % (self.jogFeed))

	def jogXPYN(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 X1000 Y-1000\n" % (self.jogFeed))
	
	def jogZP(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 Z1000\n" % (self.jogFeed))
	
	def jogZN(self) -> None:
		self.sendJogCmd(b"$J=F%f G91 Z-1000\n" % (self.jogFeed))

	def jogCancel(self) -> None:
		if not self.connected: return
		self.serial.write(b"\x85")

	def gotoZeroX(self) -> None:
		self.sendCmd(b"G0 X0\n")

	def gotoZeroY(self) -> None:
		self.sendCmd(b"G0 Y0\n")

	def gotoZeroZ(self) -> None:
		self.sendCmd(b"G0 Z0\n")

	def zeroWorkX(self) -> None:
		self.sendCmd(b"G10 L20 P0 X0\n")

	def zeroWorkY(self) -> None:
		self.sendCmd(b"G10 L20 P0 Y0\n")

	def zeroWorkZ(self) -> None:
		self.sendCmd(b"G10 L20 P0 Z0\n")

	def unlock(self) -> None:
		self.sendCmd(b"$X\n")


	def sendJogCmd(self, cmd: bytes) -> None:
		if not self.connected or self.state != "Idle": return
		self.serial.write(cmd)
		self.bytesInBuf.append(len(cmd))

	def sendCmd(self, cmd: bytes):
		self.serial.write(cmd)
		self.bytesInBuf.append(len(cmd))