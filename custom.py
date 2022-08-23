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
