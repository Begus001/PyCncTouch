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
    QLabel, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

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
        self.horizontalLayout_4 = QHBoxLayout(ViewMain)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_14 = QPushButton(ViewMain)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 100))
        self.pushButton_14.setProperty("pageIndex", 0)

        self.horizontalLayout_3.addWidget(self.pushButton_14)

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
        self.stackMain.addWidget(self.pageConnect)
        self.pageNC = QWidget()
        self.pageNC.setObjectName(u"pageNC")
        self.stackMain.addWidget(self.pageNC)
        self.pageJog = QWidget()
        self.pageJog.setObjectName(u"pageJog")
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
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_18 = QPushButton(self.groupBox_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.pushButton_18)

        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_15 = QPushButton(self.groupBox_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.groupBox_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.groupBox_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_17)


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
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton_10 = QPushButton(self.groupBox)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.pushButton_11 = QPushButton(self.groupBox)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_11)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.pushButton_12 = QPushButton(self.groupBox)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_12)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(18)
        self.label_4.setFont(font2)
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


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(ViewMain)
        self.btFeed.pressed.connect(ViewMain.setFeed)
        self.pushButton_14.pressed.connect(ViewMain.switchPage)
        self.btPageNC.pressed.connect(ViewMain.switchPage)
        self.btPageJog.pressed.connect(ViewMain.switchPage)

        self.stackMain.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(ViewMain)
    # setupUi

    def retranslateUi(self, ViewMain):
        ViewMain.setWindowTitle(QCoreApplication.translate("ViewMain", u"Form", None))
        self.pushButton_14.setText(QCoreApplication.translate("ViewMain", u"Connect", None))
        self.pushButton_14.setProperty("1", QCoreApplication.translate("ViewMain", u"1", None))
        self.btPageNC.setText(QCoreApplication.translate("ViewMain", u"NC", None))
        self.btPageJog.setText(QCoreApplication.translate("ViewMain", u"Jog", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ViewMain", u"Jog", None))
        self.pushButton_2.setText(QCoreApplication.translate("ViewMain", u"Y+", None))
        self.pushButton_3.setText(QCoreApplication.translate("ViewMain", u"X+Y+", None))
        self.pushButton_9.setText(QCoreApplication.translate("ViewMain", u"X+Y-", None))
        self.pushButton.setText(QCoreApplication.translate("ViewMain", u"X-Y+", None))
        self.pushButton_18.setText(QCoreApplication.translate("ViewMain", u"X0", None))
        self.pushButton_5.setText(QCoreApplication.translate("ViewMain", u"Y0", None))
        self.pushButton_7.setText(QCoreApplication.translate("ViewMain", u"X-Y-", None))
        self.pushButton_6.setText(QCoreApplication.translate("ViewMain", u"X+", None))
        self.pushButton_4.setText(QCoreApplication.translate("ViewMain", u"X-", None))
        self.pushButton_8.setText(QCoreApplication.translate("ViewMain", u"Y-", None))
        self.pushButton_15.setText(QCoreApplication.translate("ViewMain", u"Z+", None))
        self.pushButton_16.setText(QCoreApplication.translate("ViewMain", u"Z0", None))
        self.pushButton_17.setText(QCoreApplication.translate("ViewMain", u"Z-", None))
        self.groupBox.setTitle(QCoreApplication.translate("ViewMain", u"Position", None))
        self.label.setText(QCoreApplication.translate("ViewMain", u"X", None))
        self.pushButton_10.setText(QCoreApplication.translate("ViewMain", u"0.000", None))
        self.label_2.setText(QCoreApplication.translate("ViewMain", u"Y", None))
        self.pushButton_11.setText(QCoreApplication.translate("ViewMain", u"0.000", None))
        self.label_3.setText(QCoreApplication.translate("ViewMain", u"Z", None))
        self.pushButton_12.setText(QCoreApplication.translate("ViewMain", u"0.000", None))
        self.label_4.setText(QCoreApplication.translate("ViewMain", u"Feed", None))
        self.btFeed.setText(QCoreApplication.translate("ViewMain", u"5000", None))
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

