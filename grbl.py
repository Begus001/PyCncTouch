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
		report = report[report.index(",")+1:]
		try:
			self.currentSpeed: float = float(report[:report.index("|")])
		except ValueError:
			self.currentSpeed: float = float(report[:report.index(">")])


class GrblInterface(QObject):
	connectionChanged = Signal(bool)
	statusUpdate = Signal(GrblStatus)
	stateChanged = Signal(str)
	processedIndexChanged = Signal(int)
	streamStatusChanged = Signal(bool)
	messageReceived = Signal(str)
	messageSent = Signal(str)

	def __init__(self, defaultFeed: int, defaultIncDist: float, statusInterval: int):
		super().__init__()
		self.connected: bool = False
		self.serial = s.Serial()

		self.shouldClose: bool = False
		self.stream: bool = False
		self.gcode: str = ""

		self.jogFeed: int = defaultFeed
		self.incDist: float = defaultIncDist
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
							self.messageReceived.emit(resp)
							if len(self.bytesInBuf) > 0:
								del self.bytesInBuf[0]
						elif resp.startswith("<"):
							self.keepAlive = True
							self.state = resp[1:resp.index("|")]
							self.stateChanged.emit(self.state)
							self.statusUpdate.emit(GrblStatus(resp))
						else:
							self.messageReceived.emit(resp)
				else:
					self.processedIndexChanged.emit(0)
					lineIndex = 0
					processedIndex = 0

					for line in self.gcode.splitlines():
						line = line + "\n"
						lineIndex += 1
						self.bytesInBuf.append(len(line))

						while sum(self.bytesInBuf) > 127 or self.serial.inWaiting():
							if not self.checkAlarmAndConnected():
								self.stopStream()
								break
							
							self.mutexSerial.lock()
							resp = self.serial.readline().decode().strip()
							self.mutexSerial.unlock()

							if "ok" in resp or "error" in resp:
								processedIndex += 1
								self.processedIndexChanged.emit(processedIndex)
								self.messageReceived.emit(resp)
								if len(self.bytesInBuf) > 0:
									del self.bytesInBuf[0]
							elif "<" in resp:
								self.keepAlive = True
								self.state = resp[1:resp.index("|")]
								self.stateChanged.emit(self.state)
								self.statusUpdate.emit(GrblStatus(resp))
							elif "Grbl " in resp:
								self.keepAlive = True
								self.messageReceived.emit(resp)
								self.stopStream()
								break
							else:
								self.messageReceived.emit(resp)
						
						if not self.checkAlarmAndConnected():
							self.stopStream()
							break
						
						self.mutexSerial.lock()
						self.serial.write(line.encode())
						self.messageSent.emit(line)
						self.mutexSerial.unlock()
					
					while processedIndex < lineIndex and self.stream:

						if not self.checkAlarmAndConnected():
							self.stopStream()
							break

						resp = self.serial.readline().decode().strip()
						if "ok" in resp or "error" in resp:
								processedIndex += 1
								self.processedIndexChanged.emit(processedIndex)
								self.messageReceived.emit(resp)
								if len(self.bytesInBuf) > 0:
									del self.bytesInBuf[0]
						elif "<" in resp:
							self.keepAlive = True
							self.state = resp[1:resp.index("|")]
							self.stateChanged.emit(self.state)
							self.statusUpdate.emit(GrblStatus(resp))
						elif "Grbl " in resp:
							self.keepAlive = True
							self.messageReceived.emit(resp)
							self.stopStream()
							break
						else:
							self.messageReceived.emit(resp)
					
					self.stopStream()
						

				time.sleep(0.001)
			else:
				time.sleep(0.5)

	def checkAlarmAndConnected(self) -> bool:
		if "Alarm" not in self.state and self.connected and self.stream and self.serial.isOpen() and not self.shouldClose: return True
		else: return False

	def stopStream(self) -> None:
		self.setStream(False)
		self.serial.reset_input_buffer()
		self.bytesInBuf.clear()

	def statusLoop(self):
		while not self.shouldClose:
			time.sleep(0.5)
			while self.connected and self.serial.isOpen() and not self.shouldClose:
				self.serial.write(b"?")
				time.sleep(self.statusInterval / 1000.0)

	def connectionKeepAlive(self):
		while not self.shouldClose:
			time.sleep(1)
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
			self.stopStream()
			self.mutexSerial.lock()
			time.sleep(.2)
			self.serial.reset_input_buffer()
			self.serial.close()
			self.mutexSerial.unlock()

	def setStream(self, stream: bool) -> None:
		self.stream = stream
		self.streamStatusChanged.emit(stream)

	def connectPort(self, port: str) -> None:
		self.serial.port = port
		self.serial.baudrate = 115200
		try:
			self.serial.open()
			self.sendCmd(b"\x18", False)
			self.serial.flush()
			resp = self.serial.readline().strip().decode()
			resp = self.serial.readline().strip().decode()
			self.messageReceived.emit(resp)
			self.serial.reset_input_buffer()
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
		self.sendCmd(b"\x85", False)

	def moveXNYP(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 X-%f Y%f\n" % (self.incDist, self.incDist))
		self.sendCmd(b"G90\n")

	def moveYP(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 Y%f\n" % (self.incDist))
		self.sendCmd(b"G90\n")

	def moveXPYP(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 X%f Y%f\n" % (self.incDist, self.incDist))
		self.sendCmd(b"G90\n")

	def moveXN(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 X-%f\n" % (self.incDist))
		self.sendCmd(b"G90\n")

	def moveXP(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 X%f\n" % (self.incDist))
		self.sendCmd(b"G90\n")

	def moveXNYN(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 X-%f Y-%f\n" % (self.incDist, self.incDist))
		self.sendCmd(b"G90\n")

	def moveYN(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 Y-%f\n" % (self.incDist))
		self.sendCmd(b"G90\n")

	def moveXPYN(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 X%f Y-%f\n" % (self.incDist, self.incDist))
		self.sendCmd(b"G90\n")
	
	def moveZP(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 Z%f\n" % (self.incDist))
		self.sendCmd(b"G90\n")
	
	def moveZN(self) -> None:
		self.sendCmd(b"G91\n")
		self.sendJogCmd(b"G0 Z-%f\n" % (self.incDist))
		self.sendCmd(b"G90\n")

	def gotoZeroX(self) -> None:
		self.sendCmd(b"G0 X0\n")

	def gotoZeroY(self) -> None:
		self.sendCmd(b"G0 Y0\n")

	def gotoZeroZ(self) -> None:
		self.sendCmd(b"G0 Z0\n")

	def setX(self, val: float) -> None:
		self.sendCmd(b"G10 L20 P0 X%f\n" % (val))

	def setY(self, val: float) -> None:
		self.sendCmd(b"G10 L20 P0 Y%f\n" % (val))

	def setZ(self, val: float) -> None:
		self.sendCmd(b"G10 L20 P0 Z%f\n" % (val))

	def unlock(self) -> None:
		self.sendCmd(b"$X\n")

	def loadNC(self, gcode: str) -> None:
		self.gcode = gcode 

	def startNC(self) -> None:
		self.setStream(True)

	def sendJogCmd(self, cmd: bytes) -> None:
		if not self.connected or self.state != "Idle": return
		self.serial.write(cmd)
		self.bytesInBuf.append(len(cmd))
		self.messageSent.emit(cmd.decode())

	def sendCmd(self, cmd: bytes, waitOk: bool = True):
		self.serial.write(cmd)
		if waitOk:
			self.bytesInBuf.append(len(cmd))
			self.messageSent.emit(cmd.decode())