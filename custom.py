from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class ConnectComboBox(QComboBox):
	popup = Signal()
	def __init__(self, *args):
		super().__init__(*args)
		self.listview = QListView(self)
		self.listview.setStyleSheet("QListView::item{height: 100px}")
		self.listview.setFont(self.font())
		self.setView(self.listview)
		self.scroll = QScrollBar(Qt.Orientation.Vertical, self)
		self.scroll.setStyleSheet("QScrollBar:vertical{width:50px;}")
		self.view().setVerticalScrollBar(self.scroll)
		self.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
	
	def showPopup(self) -> None:
		self.popup.emit()
		return super().showPopup()


class GcodeViewer(QWidget):
	def __init__(self, *args):
		super().__init__(*args)
		self.gcode: str = ""
		self.gcodeIndex: int = 0
		self.xmax: float
		self.xmin: float
		self.ymax: float
		self.ymin: float
		self.scale: float

		self.curx: float = None
		self.cury: float = None

	def loadGcode(self, gcode: str) -> None:
		self.gcode = gcode
		self.gcodeIndex = 0
		self.analyzeLimits()
		self.repaint()

	def analyzeLimits(self) -> None:
		self.xmax = -1e16
		self.xmin = 1e16
		self.ymax = -1e16
		self.ymin = 1e16

		for line in self.gcode.splitlines():
			
			x = self.gcodeGetVal(line, "X")
			if x != 1e16:
				if x > self.xmax: self.xmax = x
				if x < self.xmin: self.xmin = x
			
			y = self.gcodeGetVal(line, "Y")
			if y != 1e16:
				if y > self.ymax: self.ymax = y
				if y < self.ymin: self.ymin = y

		print("Analyzed:\nX %f %f\nY %f %f" % (self.xmax, self.xmin, self.ymax, self.ymin))
		print()

		# if self.xmax > self.ymax: self.ymax = self.xmax
		# else: self.xmax = self.ymax

		# if self.xmin < self.ymin: self.ymin = self.xmin
		# else: self.xmin = self.ymin

		print("Scaled\nX %f %f\nY %f %f" % (self.xmax, self.xmin, self.ymax, self.ymin))

		self.xmax += 5
		self.xmin -= 5
		self.ymax += 5
		self.ymin -= 5

	def gcodeGetVal(self, line: str, val: str) -> float:
		if val in line:
			i = line.index(val) + 1
			while i < len(line) and (line[i].isdigit() or line[i] == "." or line[i] == "-"): i += 1
			if i == len(line):
				x = float(line[line.index(val)+1:])
			else:
				x = float(line[line.index(val)+1:i])
			return x
		else: return 1e16

	def cvtX(self, x: float) -> int:
		return int(((x - self.xmin) / (self.xmax - self.xmin)) * self.width())

	def cvtY(self, y: float) -> int:
		return int(self.height() - (((y - self.ymin) / (self.ymax - self.ymin)) * self.height()))
	
	def paintEvent(self, e: QPaintEvent) -> None:
		p = QPainter(self)
		p.fillRect(0, 0, self.width(), self.height(), Qt.white)
		try:
			x = 0
			y = 0
			px = 0
			py = 0
			draw = False
			for i, line in enumerate(self.gcode.splitlines()):
				if "G1" in line or "G2" in line or "G3" in line: draw = True
				elif "G0" in line : draw = False
				
				if not draw: continue

				if "X" not in line and "Y" not in line: continue

				if i < self.gcodeIndex: p.setPen(QPen(Qt.lightGray, 1))
				else: p.setPen(QPen(Qt.black, 2))

				tmp = self.gcodeGetVal(line, "X")
				if tmp != 1e16:
					x = tmp
				tmp = self.gcodeGetVal(line, "Y")
				if tmp != 1e16:
					y = tmp
				
				if px != x or py != y:
					p.drawLine(self.cvtX(px), self.cvtY(py), self.cvtX(x), self.cvtY(y))
				px = x
				py = y
				
			p.setPen(QPen(Qt.red, 3))
			if self.curx != None and self.cury != None and self.gcode != "":
				p.drawLine(self.cvtX(self.curx) + 10, self.cvtY(self.cury) + 10, self.cvtX(self.curx) - 10, self.cvtY(self.cury) - 10)
				p.drawLine(self.cvtX(self.curx) + 10, self.cvtY(self.cury) - 10, self.cvtX(self.curx) - 10, self.cvtY(self.cury) + 10)
		except:
			print("oh cock")
		finally:
			p.end()

