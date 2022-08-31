# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewMain.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

from custom import ConnectComboBox

class ViewMain(object):
    def setupUi(self, ViewMain):
        if not ViewMain.objectName():
            ViewMain.setObjectName(u"ViewMain")
        ViewMain.resize(1024, 600)
        ViewMain.setMinimumSize(QSize(1024, 600))
        ViewMain.setMaximumSize(QSize(1024, 600))
        font = QFont()
        font.setPointSize(16)
        ViewMain.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(ViewMain)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btPageConnect = QPushButton(ViewMain)
        self.btPageConnect.setObjectName(u"btPageConnect")
        self.btPageConnect.setMinimumSize(QSize(0, 100))
        self.btPageConnect.setProperty("pageIndex", 0)

        self.horizontalLayout_3.addWidget(self.btPageConnect)

        self.btPageNC = QPushButton(ViewMain)
        self.btPageNC.setObjectName(u"btPageNC")
        self.btPageNC.setMinimumSize(QSize(0, 100))
        self.btPageNC.setProperty("pageIndex", 1)

        self.horizontalLayout_3.addWidget(self.btPageNC)

        self.btPageJog = QPushButton(ViewMain)
        self.btPageJog.setObjectName(u"btPageJog")
        self.btPageJog.setMinimumSize(QSize(0, 100))
        self.btPageJog.setProperty("pageIndex", 2)

        self.horizontalLayout_3.addWidget(self.btPageJog)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.stackMain = QStackedWidget(ViewMain)
        self.stackMain.setObjectName(u"stackMain")
        self.pageConnect = QWidget()
        self.pageConnect.setObjectName(u"pageConnect")
        self.horizontalLayout = QHBoxLayout(self.pageConnect)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cbPorts = ConnectComboBox(self.pageConnect)
        self.cbPorts.setObjectName(u"cbPorts")
        self.cbPorts.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(30)
        self.cbPorts.setFont(font1)

        self.horizontalLayout.addWidget(self.cbPorts)

        self.btConnect = QPushButton(self.pageConnect)
        self.btConnect.setObjectName(u"btConnect")
        self.btConnect.setMinimumSize(QSize(0, 100))

        self.horizontalLayout.addWidget(self.btConnect)

        self.stackMain.addWidget(self.pageConnect)
        self.pageNC = QWidget()
        self.pageNC.setObjectName(u"pageNC")
        self.horizontalLayout_10 = QHBoxLayout(self.pageNC)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btOpen = QPushButton(self.pageNC)
        self.btOpen.setObjectName(u"btOpen")
        self.btOpen.setMinimumSize(QSize(100, 50))

        self.verticalLayout_4.addWidget(self.btOpen)

        self.btStart = QPushButton(self.pageNC)
        self.btStart.setObjectName(u"btStart")
        self.btStart.setMinimumSize(QSize(100, 50))

        self.verticalLayout_4.addWidget(self.btStart)

        self.btUnlock = QPushButton(self.pageNC)
        self.btUnlock.setObjectName(u"btUnlock")
        self.btUnlock.setMinimumSize(QSize(100, 50))

        self.verticalLayout_4.addWidget(self.btUnlock)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.listGcode = QListWidget(self.pageNC)
        self.listGcode.setObjectName(u"listGcode")

        self.horizontalLayout_9.addWidget(self.listGcode)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.stackMain.addWidget(self.pageNC)
        self.pageJog = QWidget()
        self.pageJog.setObjectName(u"pageJog")
        self.pageJog.setEnabled(False)
        self.horizontalLayout_7 = QHBoxLayout(self.pageJog)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_2 = QGroupBox(self.pageJog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btGotoZeroX = QPushButton(self.groupBox_2)
        self.btGotoZeroX.setObjectName(u"btGotoZeroX")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btGotoZeroX.sizePolicy().hasHeightForWidth())
        self.btGotoZeroX.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.btGotoZeroX)

        self.btGotoZeroY = QPushButton(self.groupBox_2)
        self.btGotoZeroY.setObjectName(u"btGotoZeroY")
        sizePolicy.setHeightForWidth(self.btGotoZeroY.sizePolicy().hasHeightForWidth())
        self.btGotoZeroY.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.btGotoZeroY)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)

        self.btJogXNYP = QPushButton(self.groupBox_2)
        self.btJogXNYP.setObjectName(u"btJogXNYP")
        sizePolicy.setHeightForWidth(self.btJogXNYP.sizePolicy().hasHeightForWidth())
        self.btJogXNYP.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btJogXNYP, 0, 0, 1, 1)

        self.btJogXNYN = QPushButton(self.groupBox_2)
        self.btJogXNYN.setObjectName(u"btJogXNYN")
        sizePolicy.setHeightForWidth(self.btJogXNYN.sizePolicy().hasHeightForWidth())
        self.btJogXNYN.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btJogXNYN, 2, 0, 1, 1)

        self.btJogYN = QPushButton(self.groupBox_2)
        self.btJogYN.setObjectName(u"btJogYN")
        sizePolicy.setHeightForWidth(self.btJogYN.sizePolicy().hasHeightForWidth())
        self.btJogYN.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btJogYN, 2, 1, 1, 1)

        self.btJogXPYN = QPushButton(self.groupBox_2)
        self.btJogXPYN.setObjectName(u"btJogXPYN")
        sizePolicy.setHeightForWidth(self.btJogXPYN.sizePolicy().hasHeightForWidth())
        self.btJogXPYN.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btJogXPYN, 2, 2, 1, 1)

        self.btJogXP = QPushButton(self.groupBox_2)
        self.btJogXP.setObjectName(u"btJogXP")
        sizePolicy.setHeightForWidth(self.btJogXP.sizePolicy().hasHeightForWidth())
        self.btJogXP.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btJogXP, 1, 2, 1, 1)

        self.btJogXPYP = QPushButton(self.groupBox_2)
        self.btJogXPYP.setObjectName(u"btJogXPYP")
        sizePolicy.setHeightForWidth(self.btJogXPYP.sizePolicy().hasHeightForWidth())
        self.btJogXPYP.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btJogXPYP, 0, 2, 1, 1)

        self.btJogYP = QPushButton(self.groupBox_2)
        self.btJogYP.setObjectName(u"btJogYP")
        sizePolicy.setHeightForWidth(self.btJogYP.sizePolicy().hasHeightForWidth())
        self.btJogYP.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btJogYP, 0, 1, 1, 1)

        self.btJogXN = QPushButton(self.groupBox_2)
        self.btJogXN.setObjectName(u"btJogXN")
        sizePolicy.setHeightForWidth(self.btJogXN.sizePolicy().hasHeightForWidth())
        self.btJogXN.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btJogXN, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btJogZP = QPushButton(self.groupBox_2)
        self.btJogZP.setObjectName(u"btJogZP")
        sizePolicy.setHeightForWidth(self.btJogZP.sizePolicy().hasHeightForWidth())
        self.btJogZP.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btJogZP)

        self.btGotoZeroZ = QPushButton(self.groupBox_2)
        self.btGotoZeroZ.setObjectName(u"btGotoZeroZ")
        sizePolicy.setHeightForWidth(self.btGotoZeroZ.sizePolicy().hasHeightForWidth())
        self.btGotoZeroZ.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btGotoZeroZ)

        self.btJogZN = QPushButton(self.groupBox_2)
        self.btJogZN.setObjectName(u"btJogZN")
        sizePolicy.setHeightForWidth(self.btJogZN.sizePolicy().hasHeightForWidth())
        self.btJogZN.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btJogZN)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.pageJog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.btSetX = QPushButton(self.groupBox)
        self.btSetX.setObjectName(u"btSetX")
        sizePolicy.setHeightForWidth(self.btSetX.sizePolicy().hasHeightForWidth())
        self.btSetX.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btSetX)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.btSetY = QPushButton(self.groupBox)
        self.btSetY.setObjectName(u"btSetY")
        sizePolicy.setHeightForWidth(self.btSetY.sizePolicy().hasHeightForWidth())
        self.btSetY.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btSetY)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.btSetZ = QPushButton(self.groupBox)
        self.btSetZ.setObjectName(u"btSetZ")
        sizePolicy.setHeightForWidth(self.btSetZ.sizePolicy().hasHeightForWidth())
        self.btSetZ.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btSetZ)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(18)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.btFeed = QPushButton(self.groupBox)
        self.btFeed.setObjectName(u"btFeed")
        sizePolicy.setHeightForWidth(self.btFeed.sizePolicy().hasHeightForWidth())
        self.btFeed.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btFeed)

        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 7)
        self.verticalLayout_2.setStretch(3, 10)
        self.verticalLayout_2.setStretch(4, 7)
        self.verticalLayout_2.setStretch(5, 10)
        self.verticalLayout_2.setStretch(6, 10)
        self.verticalLayout_2.setStretch(7, 10)

        self.horizontalLayout_7.addWidget(self.groupBox)

        self.horizontalLayout_7.setStretch(0, 5)
        self.horizontalLayout_7.setStretch(1, 1)
        self.stackMain.addWidget(self.pageJog)

        self.verticalLayout_3.addWidget(self.stackMain)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbConnected = QLabel(ViewMain)
        self.lbConnected.setObjectName(u"lbConnected")
        self.lbConnected.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.lbConnected)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbX = QLabel(ViewMain)
        self.lbX.setObjectName(u"lbX")

        self.horizontalLayout_4.addWidget(self.lbX)

        self.lbY = QLabel(ViewMain)
        self.lbY.setObjectName(u"lbY")

        self.horizontalLayout_4.addWidget(self.lbY)

        self.lbZ = QLabel(ViewMain)
        self.lbZ.setObjectName(u"lbZ")

        self.horizontalLayout_4.addWidget(self.lbZ)

        self.lbF = QLabel(ViewMain)
        self.lbF.setObjectName(u"lbF")

        self.horizontalLayout_4.addWidget(self.lbF)

        self.lbS = QLabel(ViewMain)
        self.lbS.setObjectName(u"lbS")

        self.horizontalLayout_4.addWidget(self.lbS)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)

        self.lbState = QLabel(ViewMain)
        self.lbState.setObjectName(u"lbState")
        self.lbState.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lbState)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.retranslateUi(ViewMain)
        self.btFeed.pressed.connect(ViewMain.setFeed)
        self.btPageConnect.pressed.connect(ViewMain.switchPage)
        self.btPageNC.pressed.connect(ViewMain.switchPage)
        self.btPageJog.pressed.connect(ViewMain.switchPage)
        self.cbPorts.popup.connect(ViewMain.fillDevices)
        self.btConnect.pressed.connect(ViewMain.connectPort)
        self.btJogXNYP.pressed.connect(ViewMain.jogXNYP)
        self.btJogYP.pressed.connect(ViewMain.jogYP)
        self.btJogXPYP.pressed.connect(ViewMain.jogXPYP)
        self.btJogXN.pressed.connect(ViewMain.jogXN)
        self.btJogXP.pressed.connect(ViewMain.jogXP)
        self.btJogXNYN.pressed.connect(ViewMain.jogXNYN)
        self.btJogYN.pressed.connect(ViewMain.jogYN)
        self.btJogXPYN.pressed.connect(ViewMain.jogXPYN)
        self.btJogZP.pressed.connect(ViewMain.jogZP)
        self.btJogZN.pressed.connect(ViewMain.jogZN)
        self.btJogXNYP.released.connect(ViewMain.jogCancel)
        self.btJogYP.released.connect(ViewMain.jogCancel)
        self.btJogXPYP.released.connect(ViewMain.jogCancel)
        self.btJogXN.released.connect(ViewMain.jogCancel)
        self.btJogXP.released.connect(ViewMain.jogCancel)
        self.btJogXNYN.released.connect(ViewMain.jogCancel)
        self.btJogYN.released.connect(ViewMain.jogCancel)
        self.btJogXPYN.released.connect(ViewMain.jogCancel)
        self.btJogZP.released.connect(ViewMain.jogCancel)
        self.btJogZN.released.connect(ViewMain.jogCancel)
        self.btGotoZeroX.pressed.connect(ViewMain.gotoZeroX)
        self.btGotoZeroY.pressed.connect(ViewMain.gotoZeroY)
        self.btGotoZeroZ.pressed.connect(ViewMain.gotoZeroZ)
        self.btSetX.pressed.connect(ViewMain.setWorkX)
        self.btSetY.pressed.connect(ViewMain.setWorkY)
        self.btSetZ.pressed.connect(ViewMain.setWorkZ)
        self.btOpen.pressed.connect(ViewMain.openNC)
        self.btStart.pressed.connect(ViewMain.startNC)
        self.btUnlock.pressed.connect(ViewMain.unlock)

        QMetaObject.connectSlotsByName(ViewMain)
    # setupUi

    def retranslateUi(self, ViewMain):
        ViewMain.setWindowTitle(QCoreApplication.translate("ViewMain", u"Form", None))
        self.btPageConnect.setText(QCoreApplication.translate("ViewMain", u"Connect", None))
        self.btPageConnect.setProperty("1", QCoreApplication.translate("ViewMain", u"1", None))
        self.btPageNC.setText(QCoreApplication.translate("ViewMain", u"NC", None))
        self.btPageJog.setText(QCoreApplication.translate("ViewMain", u"Jog", None))
        self.btConnect.setText(QCoreApplication.translate("ViewMain", u"Connect", None))
        self.btOpen.setText(QCoreApplication.translate("ViewMain", u"Open", None))
        self.btStart.setText(QCoreApplication.translate("ViewMain", u"Start", None))
        self.btUnlock.setText(QCoreApplication.translate("ViewMain", u"Unlock", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ViewMain", u"Jog", None))
        self.btGotoZeroX.setText(QCoreApplication.translate("ViewMain", u"X0", None))
        self.btGotoZeroY.setText(QCoreApplication.translate("ViewMain", u"Y0", None))
        self.btJogXNYP.setText(QCoreApplication.translate("ViewMain", u"X-Y+", None))
        self.btJogXNYN.setText(QCoreApplication.translate("ViewMain", u"X-Y-", None))
        self.btJogYN.setText(QCoreApplication.translate("ViewMain", u"Y-", None))
        self.btJogXPYN.setText(QCoreApplication.translate("ViewMain", u"X+Y-", None))
        self.btJogXP.setText(QCoreApplication.translate("ViewMain", u"X+", None))
        self.btJogXPYP.setText(QCoreApplication.translate("ViewMain", u"X+Y+", None))
        self.btJogYP.setText(QCoreApplication.translate("ViewMain", u"Y+", None))
        self.btJogXN.setText(QCoreApplication.translate("ViewMain", u"X-", None))
        self.btJogZP.setText(QCoreApplication.translate("ViewMain", u"Z+", None))
        self.btGotoZeroZ.setText(QCoreApplication.translate("ViewMain", u"Z0", None))
        self.btJogZN.setText(QCoreApplication.translate("ViewMain", u"Z-", None))
        self.groupBox.setTitle(QCoreApplication.translate("ViewMain", u"Position", None))
        self.label.setText(QCoreApplication.translate("ViewMain", u"X", None))
        self.btSetX.setText(QCoreApplication.translate("ViewMain", u"0.000", None))
        self.label_2.setText(QCoreApplication.translate("ViewMain", u"Y", None))
        self.btSetY.setText(QCoreApplication.translate("ViewMain", u"0.000", None))
        self.label_3.setText(QCoreApplication.translate("ViewMain", u"Z", None))
        self.btSetZ.setText(QCoreApplication.translate("ViewMain", u"0.000", None))
        self.label_4.setText(QCoreApplication.translate("ViewMain", u"Feed", None))
        self.btFeed.setText(QCoreApplication.translate("ViewMain", u"5000", None))
        self.lbConnected.setText(QCoreApplication.translate("ViewMain", u"Disconnected", None))
        self.lbX.setText(QCoreApplication.translate("ViewMain", u"X0.000", None))
        self.lbY.setText(QCoreApplication.translate("ViewMain", u"Y0.000", None))
        self.lbZ.setText(QCoreApplication.translate("ViewMain", u"Z0.000", None))
        self.lbF.setText(QCoreApplication.translate("ViewMain", u"F0.0", None))
        self.lbS.setText(QCoreApplication.translate("ViewMain", u"S0", None))
        self.lbState.setText(QCoreApplication.translate("ViewMain", u"Idle", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewFeed.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QWidget)

class ViewFeed(object):
    def setupUi(self, ViewFeed):
        if not ViewFeed.objectName():
            ViewFeed.setObjectName(u"ViewFeed")
        ViewFeed.resize(1024, 600)
        self.gridLayout = QGridLayout(ViewFeed)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bt01 = QPushButton(ViewFeed)
        self.bt01.setObjectName(u"bt01")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt01.sizePolicy().hasHeightForWidth())
        self.bt01.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        self.bt01.setFont(font)

        self.gridLayout.addWidget(self.bt01, 0, 0, 1, 1)

        self.bt02 = QPushButton(ViewFeed)
        self.bt02.setObjectName(u"bt02")
        sizePolicy.setHeightForWidth(self.bt02.sizePolicy().hasHeightForWidth())
        self.bt02.setSizePolicy(sizePolicy)
        self.bt02.setFont(font)

        self.gridLayout.addWidget(self.bt02, 0, 1, 1, 1)

        self.bt03 = QPushButton(ViewFeed)
        self.bt03.setObjectName(u"bt03")
        sizePolicy.setHeightForWidth(self.bt03.sizePolicy().hasHeightForWidth())
        self.bt03.setSizePolicy(sizePolicy)
        self.bt03.setFont(font)

        self.gridLayout.addWidget(self.bt03, 0, 2, 1, 1)

        self.bt04 = QPushButton(ViewFeed)
        self.bt04.setObjectName(u"bt04")
        sizePolicy.setHeightForWidth(self.bt04.sizePolicy().hasHeightForWidth())
        self.bt04.setSizePolicy(sizePolicy)
        self.bt04.setFont(font)

        self.gridLayout.addWidget(self.bt04, 0, 3, 1, 1)

        self.bt05 = QPushButton(ViewFeed)
        self.bt05.setObjectName(u"bt05")
        sizePolicy.setHeightForWidth(self.bt05.sizePolicy().hasHeightForWidth())
        self.bt05.setSizePolicy(sizePolicy)
        self.bt05.setFont(font)

        self.gridLayout.addWidget(self.bt05, 1, 0, 1, 1)

        self.bt06 = QPushButton(ViewFeed)
        self.bt06.setObjectName(u"bt06")
        sizePolicy.setHeightForWidth(self.bt06.sizePolicy().hasHeightForWidth())
        self.bt06.setSizePolicy(sizePolicy)
        self.bt06.setFont(font)

        self.gridLayout.addWidget(self.bt06, 1, 1, 1, 1)

        self.bt07 = QPushButton(ViewFeed)
        self.bt07.setObjectName(u"bt07")
        sizePolicy.setHeightForWidth(self.bt07.sizePolicy().hasHeightForWidth())
        self.bt07.setSizePolicy(sizePolicy)
        self.bt07.setFont(font)

        self.gridLayout.addWidget(self.bt07, 1, 2, 1, 1)

        self.bt08 = QPushButton(ViewFeed)
        self.bt08.setObjectName(u"bt08")
        sizePolicy.setHeightForWidth(self.bt08.sizePolicy().hasHeightForWidth())
        self.bt08.setSizePolicy(sizePolicy)
        self.bt08.setFont(font)

        self.gridLayout.addWidget(self.bt08, 1, 3, 1, 1)

        self.bt09 = QPushButton(ViewFeed)
        self.bt09.setObjectName(u"bt09")
        sizePolicy.setHeightForWidth(self.bt09.sizePolicy().hasHeightForWidth())
        self.bt09.setSizePolicy(sizePolicy)
        self.bt09.setFont(font)

        self.gridLayout.addWidget(self.bt09, 2, 0, 1, 1)

        self.bt10 = QPushButton(ViewFeed)
        self.bt10.setObjectName(u"bt10")
        sizePolicy.setHeightForWidth(self.bt10.sizePolicy().hasHeightForWidth())
        self.bt10.setSizePolicy(sizePolicy)
        self.bt10.setFont(font)

        self.gridLayout.addWidget(self.bt10, 2, 1, 1, 1)

        self.bt11 = QPushButton(ViewFeed)
        self.bt11.setObjectName(u"bt11")
        sizePolicy.setHeightForWidth(self.bt11.sizePolicy().hasHeightForWidth())
        self.bt11.setSizePolicy(sizePolicy)
        self.bt11.setFont(font)

        self.gridLayout.addWidget(self.bt11, 2, 2, 1, 1)

        self.bt12 = QPushButton(ViewFeed)
        self.bt12.setObjectName(u"bt12")
        sizePolicy.setHeightForWidth(self.bt12.sizePolicy().hasHeightForWidth())
        self.bt12.setSizePolicy(sizePolicy)
        self.bt12.setFont(font)

        self.gridLayout.addWidget(self.bt12, 2, 3, 1, 1)

        self.bt13 = QPushButton(ViewFeed)
        self.bt13.setObjectName(u"bt13")
        sizePolicy.setHeightForWidth(self.bt13.sizePolicy().hasHeightForWidth())
        self.bt13.setSizePolicy(sizePolicy)
        self.bt13.setFont(font)

        self.gridLayout.addWidget(self.bt13, 3, 0, 1, 1)

        self.bt14 = QPushButton(ViewFeed)
        self.bt14.setObjectName(u"bt14")
        sizePolicy.setHeightForWidth(self.bt14.sizePolicy().hasHeightForWidth())
        self.bt14.setSizePolicy(sizePolicy)
        self.bt14.setFont(font)

        self.gridLayout.addWidget(self.bt14, 3, 1, 1, 1)

        self.bt15 = QPushButton(ViewFeed)
        self.bt15.setObjectName(u"bt15")
        sizePolicy.setHeightForWidth(self.bt15.sizePolicy().hasHeightForWidth())
        self.bt15.setSizePolicy(sizePolicy)
        self.bt15.setFont(font)

        self.gridLayout.addWidget(self.bt15, 3, 2, 1, 1)

        self.bt16 = QPushButton(ViewFeed)
        self.bt16.setObjectName(u"bt16")
        sizePolicy.setHeightForWidth(self.bt16.sizePolicy().hasHeightForWidth())
        self.bt16.setSizePolicy(sizePolicy)
        self.bt16.setFont(font)

        self.gridLayout.addWidget(self.bt16, 3, 3, 1, 1)


        self.retranslateUi(ViewFeed)
        self.bt01.pressed.connect(ViewFeed.returnFeed)
        self.bt02.pressed.connect(ViewFeed.returnFeed)
        self.bt03.pressed.connect(ViewFeed.returnFeed)
        self.bt04.pressed.connect(ViewFeed.returnFeed)
        self.bt05.pressed.connect(ViewFeed.returnFeed)
        self.bt06.pressed.connect(ViewFeed.returnFeed)
        self.bt07.pressed.connect(ViewFeed.returnFeed)
        self.bt08.pressed.connect(ViewFeed.returnFeed)
        self.bt09.pressed.connect(ViewFeed.returnFeed)
        self.bt10.pressed.connect(ViewFeed.returnFeed)
        self.bt11.pressed.connect(ViewFeed.returnFeed)
        self.bt12.pressed.connect(ViewFeed.returnFeed)
        self.bt13.pressed.connect(ViewFeed.returnFeed)
        self.bt14.pressed.connect(ViewFeed.returnFeed)
        self.bt15.pressed.connect(ViewFeed.returnFeed)
        self.bt16.pressed.connect(ViewFeed.returnFeed)

        QMetaObject.connectSlotsByName(ViewFeed)
    # setupUi

    def retranslateUi(self, ViewFeed):
        ViewFeed.setWindowTitle(QCoreApplication.translate("ViewFeed", u"Dialog", None))
        self.bt01.setText(QCoreApplication.translate("ViewFeed", u"1", None))
        self.bt02.setText(QCoreApplication.translate("ViewFeed", u"10", None))
        self.bt03.setText(QCoreApplication.translate("ViewFeed", u"50", None))
        self.bt04.setText(QCoreApplication.translate("ViewFeed", u"100", None))
        self.bt05.setText(QCoreApplication.translate("ViewFeed", u"200", None))
        self.bt06.setText(QCoreApplication.translate("ViewFeed", u"300", None))
        self.bt07.setText(QCoreApplication.translate("ViewFeed", u"500", None))
        self.bt08.setText(QCoreApplication.translate("ViewFeed", u"1000", None))
        self.bt09.setText(QCoreApplication.translate("ViewFeed", u"1500", None))
        self.bt10.setText(QCoreApplication.translate("ViewFeed", u"2000", None))
        self.bt11.setText(QCoreApplication.translate("ViewFeed", u"2500", None))
        self.bt12.setText(QCoreApplication.translate("ViewFeed", u"3000", None))
        self.bt13.setText(QCoreApplication.translate("ViewFeed", u"3500", None))
        self.bt14.setText(QCoreApplication.translate("ViewFeed", u"4000", None))
        self.bt15.setText(QCoreApplication.translate("ViewFeed", u"4500", None))
        self.bt16.setText(QCoreApplication.translate("ViewFeed", u"5000", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewOpen.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class ViewOpen(object):
    def setupUi(self, ViewOpen):
        if not ViewOpen.objectName():
            ViewOpen.setObjectName(u"ViewOpen")
        ViewOpen.resize(1024, 600)
        self.listFiles = QListWidget(ViewOpen)
        self.listFiles.setObjectName(u"listFiles")
        self.listFiles.setGeometry(QRect(10, 10, 871, 561))
        self.btOpen = QPushButton(ViewOpen)
        self.btOpen.setObjectName(u"btOpen")
        self.btOpen.setGeometry(QRect(910, 40, 101, 61))
        self.btCancel = QPushButton(ViewOpen)
        self.btCancel.setObjectName(u"btCancel")
        self.btCancel.setGeometry(QRect(910, 120, 101, 71))

        self.retranslateUi(ViewOpen)
        self.btOpen.pressed.connect(ViewOpen.returnFile)
        self.btCancel.pressed.connect(ViewOpen.cancel)

        QMetaObject.connectSlotsByName(ViewOpen)
    # setupUi

    def retranslateUi(self, ViewOpen):
        ViewOpen.setWindowTitle(QCoreApplication.translate("ViewOpen", u"Dialog", None))
        self.btOpen.setText(QCoreApplication.translate("ViewOpen", u"Open", None))
        self.btCancel.setText(QCoreApplication.translate("ViewOpen", u"Cancel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewSetAxis.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class ViewSetAxis(object):
    def setupUi(self, ViewSetAxis):
        if not ViewSetAxis.objectName():
            ViewSetAxis.setObjectName(u"ViewSetAxis")
        ViewSetAxis.resize(1024, 600)
        font = QFont()
        font.setPointSize(20)
        ViewSetAxis.setFont(font)
        self.verticalLayout = QVBoxLayout(ViewSetAxis)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btZero = QPushButton(ViewSetAxis)
        self.btZero.setObjectName(u"btZero")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btZero.sizePolicy().hasHeightForWidth())
        self.btZero.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btZero)

        self.btHalf = QPushButton(ViewSetAxis)
        self.btHalf.setObjectName(u"btHalf")
        sizePolicy.setHeightForWidth(self.btHalf.sizePolicy().hasHeightForWidth())
        self.btHalf.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btHalf)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbValue = QLabel(ViewSetAxis)
        self.lbValue.setObjectName(u"lbValue")
        self.lbValue.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbValue)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.bt1 = QPushButton(ViewSetAxis)
        self.bt1.setObjectName(u"bt1")
        sizePolicy.setHeightForWidth(self.bt1.sizePolicy().hasHeightForWidth())
        self.bt1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt1, 0, 0, 1, 1)

        self.bt2 = QPushButton(ViewSetAxis)
        self.bt2.setObjectName(u"bt2")
        sizePolicy.setHeightForWidth(self.bt2.sizePolicy().hasHeightForWidth())
        self.bt2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt2, 0, 1, 1, 1)

        self.bt3 = QPushButton(ViewSetAxis)
        self.bt3.setObjectName(u"bt3")
        sizePolicy.setHeightForWidth(self.bt3.sizePolicy().hasHeightForWidth())
        self.bt3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt3, 0, 2, 1, 1)

        self.bt4 = QPushButton(ViewSetAxis)
        self.bt4.setObjectName(u"bt4")
        sizePolicy.setHeightForWidth(self.bt4.sizePolicy().hasHeightForWidth())
        self.bt4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt4, 1, 0, 1, 1)

        self.bt5 = QPushButton(ViewSetAxis)
        self.bt5.setObjectName(u"bt5")
        sizePolicy.setHeightForWidth(self.bt5.sizePolicy().hasHeightForWidth())
        self.bt5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt5, 1, 1, 1, 1)

        self.bt6 = QPushButton(ViewSetAxis)
        self.bt6.setObjectName(u"bt6")
        sizePolicy.setHeightForWidth(self.bt6.sizePolicy().hasHeightForWidth())
        self.bt6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt6, 1, 2, 1, 1)

        self.bt7 = QPushButton(ViewSetAxis)
        self.bt7.setObjectName(u"bt7")
        sizePolicy.setHeightForWidth(self.bt7.sizePolicy().hasHeightForWidth())
        self.bt7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt7, 2, 0, 1, 1)

        self.bt8 = QPushButton(ViewSetAxis)
        self.bt8.setObjectName(u"bt8")
        sizePolicy.setHeightForWidth(self.bt8.sizePolicy().hasHeightForWidth())
        self.bt8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt8, 2, 1, 1, 1)

        self.bt9 = QPushButton(ViewSetAxis)
        self.bt9.setObjectName(u"bt9")
        sizePolicy.setHeightForWidth(self.bt9.sizePolicy().hasHeightForWidth())
        self.bt9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt9, 2, 2, 1, 1)

        self.btComma = QPushButton(ViewSetAxis)
        self.btComma.setObjectName(u"btComma")
        sizePolicy.setHeightForWidth(self.btComma.sizePolicy().hasHeightForWidth())
        self.btComma.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btComma, 3, 0, 1, 1)

        self.bt0 = QPushButton(ViewSetAxis)
        self.bt0.setObjectName(u"bt0")
        sizePolicy.setHeightForWidth(self.bt0.sizePolicy().hasHeightForWidth())
        self.bt0.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt0, 3, 1, 1, 1)

        self.btBack = QPushButton(ViewSetAxis)
        self.btBack.setObjectName(u"btBack")
        sizePolicy.setHeightForWidth(self.btBack.sizePolicy().hasHeightForWidth())
        self.btBack.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btBack, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btCancel = QPushButton(ViewSetAxis)
        self.btCancel.setObjectName(u"btCancel")
        sizePolicy.setHeightForWidth(self.btCancel.sizePolicy().hasHeightForWidth())
        self.btCancel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btCancel)

        self.btOkPositive = QPushButton(ViewSetAxis)
        self.btOkPositive.setObjectName(u"btOkPositive")
        sizePolicy.setHeightForWidth(self.btOkPositive.sizePolicy().hasHeightForWidth())
        self.btOkPositive.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btOkPositive)

        self.btOkNegative = QPushButton(ViewSetAxis)
        self.btOkNegative.setObjectName(u"btOkNegative")
        sizePolicy.setHeightForWidth(self.btOkNegative.sizePolicy().hasHeightForWidth())
        self.btOkNegative.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btOkNegative)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(ViewSetAxis)
        self.bt0.pressed.connect(ViewSetAxis.keypadEntry)
        self.bt1.pressed.connect(ViewSetAxis.keypadEntry)
        self.bt2.pressed.connect(ViewSetAxis.keypadEntry)
        self.bt3.pressed.connect(ViewSetAxis.keypadEntry)
        self.bt4.pressed.connect(ViewSetAxis.keypadEntry)
        self.bt5.pressed.connect(ViewSetAxis.keypadEntry)
        self.bt6.pressed.connect(ViewSetAxis.keypadEntry)
        self.bt7.pressed.connect(ViewSetAxis.keypadEntry)
        self.bt8.pressed.connect(ViewSetAxis.keypadEntry)
        self.bt9.pressed.connect(ViewSetAxis.keypadEntry)
        self.btBack.pressed.connect(ViewSetAxis.keypadEntry)
        self.btComma.pressed.connect(ViewSetAxis.keypadEntry)
        self.btZero.pressed.connect(ViewSetAxis.returnZero)
        self.btHalf.pressed.connect(ViewSetAxis.returnHalf)
        self.btOkPositive.pressed.connect(ViewSetAxis.returnValue)
        self.btOkNegative.pressed.connect(ViewSetAxis.returnValueNegative)
        self.btCancel.pressed.connect(ViewSetAxis.cancel)

        QMetaObject.connectSlotsByName(ViewSetAxis)
    # setupUi

    def retranslateUi(self, ViewSetAxis):
        ViewSetAxis.setWindowTitle(QCoreApplication.translate("ViewSetAxis", u"Dialog", None))
        self.btZero.setText(QCoreApplication.translate("ViewSetAxis", u"Zero", None))
        self.btHalf.setText(QCoreApplication.translate("ViewSetAxis", u"Half", None))
        self.lbValue.setText("")
        self.bt1.setText(QCoreApplication.translate("ViewSetAxis", u"1", None))
        self.bt2.setText(QCoreApplication.translate("ViewSetAxis", u"2", None))
        self.bt3.setText(QCoreApplication.translate("ViewSetAxis", u"3", None))
        self.bt4.setText(QCoreApplication.translate("ViewSetAxis", u"4", None))
        self.bt5.setText(QCoreApplication.translate("ViewSetAxis", u"5", None))
        self.bt6.setText(QCoreApplication.translate("ViewSetAxis", u"6", None))
        self.bt7.setText(QCoreApplication.translate("ViewSetAxis", u"7", None))
        self.bt8.setText(QCoreApplication.translate("ViewSetAxis", u"8", None))
        self.bt9.setText(QCoreApplication.translate("ViewSetAxis", u"9", None))
        self.btComma.setText(QCoreApplication.translate("ViewSetAxis", u".", None))
        self.bt0.setText(QCoreApplication.translate("ViewSetAxis", u"0", None))
        self.btBack.setText(QCoreApplication.translate("ViewSetAxis", u"Backspace", None))
        self.btCancel.setText(QCoreApplication.translate("ViewSetAxis", u"Cancel", None))
        self.btOkPositive.setText(QCoreApplication.translate("ViewSetAxis", u"OK Positive", None))
        self.btOkNegative.setText(QCoreApplication.translate("ViewSetAxis", u"OK Negative", None))
    # retranslateUi

