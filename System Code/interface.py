# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from mLineEdit import MLineEdit
from Custom_Widgets.Widgets import FormProgressIndicator
from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import resources1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 527)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777, 16777215))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	border: none;\n"
"}\n"
"\n"
"#leftMenu,#frame_11{\n"
"	background-color:#2596be;\n"
"	border-radius: 8px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"\n"
"#appHeader{\n"
"	color: #2596be;\n"
"}\n"
"#card1, #card2, #card3, #card4 {\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}\n"
"#pushButton, #pushButton_2{\n"
"	background-color: #2596be;\n"
"	color: #fff;\n"
"	border-radius: 10px;\n"
"}\n"
"#widget_4, #widget_5, #profileCont, #frame_15{\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}\n"
"#headerFrame{\n"
"	background-color: #fefeff;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.leftMenu.setMaximumSize(QSize(200, 527))
        self.leftMenu.setStyleSheet(u"#homeBtn{\n"
"	background-color: #fefeff;\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"	border-top-left-radius: 22px ;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.leftMenu)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_11)
        self.label_48.setObjectName(u"label_48")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Lucida Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setFrameShadow(QFrame.Plain)
        self.label_48.setScaledContents(False)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_48)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setMinimumSize(QSize(150, 0))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 11, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        font1 = QFont()
        font1.setPointSize(6)
        self.frame_14.setFont(font1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.homeBtn = QPushButton(self.frame_14)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy2)
        self.homeBtn.setMinimumSize(QSize(190, 0))
        font2 = QFont()
        font2.setFamily(u"\u5b8b\u4f53")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.homeBtn.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(35, 35))

        self.verticalLayout_11.addWidget(self.homeBtn)

        self.ocrBtn = QPushButton(self.frame_14)
        self.ocrBtn.setObjectName(u"ocrBtn")
        self.ocrBtn.setMinimumSize(QSize(190, 0))
        self.ocrBtn.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u"icons/ocr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ocrBtn.setIcon(icon1)
        self.ocrBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_11.addWidget(self.ocrBtn)

        self.percentBtn = QPushButton(self.frame_14)
        self.percentBtn.setObjectName(u"percentBtn")
        self.percentBtn.setMinimumSize(QSize(190, 0))
        self.percentBtn.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u"icons/percentage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.percentBtn.setIcon(icon2)
        self.percentBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_11.addWidget(self.percentBtn)

        self.barBtn = QPushButton(self.frame_14)
        self.barBtn.setObjectName(u"barBtn")
        self.barBtn.setMinimumSize(QSize(190, 0))
        self.barBtn.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u"icons/statistic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.barBtn.setIcon(icon3)
        self.barBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_11.addWidget(self.barBtn)

        self.pieBtn = QPushButton(self.frame_14)
        self.pieBtn.setObjectName(u"pieBtn")
        self.pieBtn.setMinimumSize(QSize(190, 0))
        self.pieBtn.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u"icons/pie.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pieBtn.setIcon(icon4)
        self.pieBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_11.addWidget(self.pieBtn)


        self.verticalLayout_12.addWidget(self.frame_14, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, 0, -1)

        self.verticalLayout_9.addWidget(self.frame_12)


        self.verticalLayout_8.addWidget(self.frame_11)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(814, 527))
        self.stackedWidget.setMaximumSize(QSize(1150, 600))
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"#homePage{\n"
"	background-color: #eff9fe;\n"
"}\n"
"#searchFrame_2{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #a8cded;\n"
"}\n"
"#lineEdit_2{\n"
"background: transparent;\n"
"	color: #78b1ff;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_18 = QHBoxLayout(self.homePage)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.mainBody = QWidget(self.homePage)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.mainBody)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.mainBody)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(780, 0))
        self.headerFrame.setMaximumSize(QSize(16777, 90))
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.headerFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(49, 0))
        self.menuBtn.setMaximumSize(QSize(49, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon5)
        self.menuBtn.setIconSize(QSize(48, 48))

        self.horizontalLayout_3.addWidget(self.menuBtn)

        self.appHeader = QLabel(self.widget)
        self.appHeader.setObjectName(u"appHeader")
        font3 = QFont()
        font3.setFamily(u"\u534e\u6587\u6977\u4f53")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.appHeader.setFont(font3)

        self.horizontalLayout_3.addWidget(self.appHeader)


        self.horizontalLayout_2.addWidget(self.widget)

        self.searchFrame_2 = QWidget(self.headerFrame)
        self.searchFrame_2.setObjectName(u"searchFrame_2")
        self.searchFrame_2.setMinimumSize(QSize(500, 40))
        self.searchFrame_2.setMaximumSize(QSize(230, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.searchFrame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.label_3 = QLabel(self.searchFrame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 30))
        self.label_3.setMaximumSize(QSize(30, 30))
        self.label_3.setPixmap(QPixmap(u":/icons/find.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.lineEdit_2 = MLineEdit(self.searchFrame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy4)
        self.lineEdit_2.setMinimumSize(QSize(400, 30))
        self.lineEdit_2.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setFamily(u"Lucida Sans Typewriter")
        font4.setPointSize(13)
        font4.setItalic(False)
        self.lineEdit_2.setFont(font4)

        self.horizontalLayout_7.addWidget(self.lineEdit_2)


        self.horizontalLayout_2.addWidget(self.searchFrame_2)

        self.widget_3 = QWidget(self.headerFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountBtn = QPushButton(self.widget_3)
        self.accountBtn.setObjectName(u"accountBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn.setIcon(icon6)
        self.accountBtn.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.accountBtn, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.headerFrame)

        self.mainFrame = QWidget(self.mainBody)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy5)
        font5 = QFont()
        font5.setPointSize(10)
        self.mainFrame.setFont(font5)
        self.horizontalLayout_12 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 8)
        self.widget_4 = QWidget(self.mainFrame)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.widget_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 54))
        self.frame_5.setMaximumSize(QSize(16777215, 60))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        font6 = QFont()
        font6.setFamily(u"\u9ed1\u4f53")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_14.setFont(font6)

        self.horizontalLayout_13.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        font7 = QFont()
        font7.setFamily(u"\u65b0\u5b8b\u4f53")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.pushButton.setFont(font7)
        icon7 = QIcon()
        icon7.addFile(u":/blueIcons/icon/blue/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_13.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.cpu_info_frame = QFrame(self.widget_4)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setMinimumSize(QSize(0, 160))
        self.cpu_info_frame.setStyleSheet(u"#cpu_info_frame,#cpu_count,#cpu_main_core{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"#cpu_per{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #fa6463;\n"
"}")
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.cpu_info_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_15 = QLabel(self.cpu_info_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(90, 16777215))
        font8 = QFont()
        font8.setFamily(u"\u5b8b\u4f53")
        font8.setBold(True)
        font8.setWeight(75)
        self.label_15.setFont(font8)

        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)

        self.cpu_main_core = QLabel(self.cpu_info_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")
        self.cpu_main_core.setMaximumSize(QSize(90, 16777215))
        font9 = QFont()
        font9.setFamily(u"Calibri")
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setWeight(50)
        self.cpu_main_core.setFont(font9)
        self.cpu_main_core.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.cpu_main_core, 2, 1, 1, 1)

        self.cpu_per = QLabel(self.cpu_info_frame)
        self.cpu_per.setObjectName(u"cpu_per")
        self.cpu_per.setMaximumSize(QSize(90, 16777215))
        self.cpu_per.setFont(font9)
        self.cpu_per.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.cpu_per, 1, 1, 1, 1)

        self.label_17 = QLabel(self.cpu_info_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(90, 16777215))
        self.label_17.setFont(font8)

        self.gridLayout.addWidget(self.label_17, 2, 0, 1, 1)

        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setMaximumSize(QSize(50, 16777215))
        self.cpu_count.setFont(font9)
        self.cpu_count.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.cpu_count, 0, 1, 1, 1)

        self.label_10 = QLabel(self.cpu_info_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(90, 16777215))
        self.label_10.setFont(font8)

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.cpu_percentage = roundProgressBar(self.cpu_info_frame)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setEnabled(True)
        self.cpu_percentage.setMinimumSize(QSize(150, 140))
        self.cpu_percentage.setMaximumSize(QSize(8888, 8888))
        self.cpu_percentage.setSizeIncrement(QSize(0, 0))

        self.gridLayout.addWidget(self.cpu_percentage, 0, 2, 3, 1, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.widget_4)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setMinimumSize(QSize(0, 180))
        self.ram_info_frame.setFont(font5)
        self.ram_info_frame.setStyleSheet(u"#ram_info_frame,#total_ram{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"#available_ram{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #99CCCC;\n"
"}\n"
"#used_ram{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #FFCC99;\n"
"}\n"
"#free_ram{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #FFCCCC;\n"
"}\n"
"\n"
"\n"
"")
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.ram_info_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.used_ram = QLabel(self.ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")
        self.used_ram.setMinimumSize(QSize(95, 37))
        self.used_ram.setMaximumSize(QSize(95, 50))
        self.used_ram.setFont(font9)
        self.used_ram.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.used_ram, 2, 1, 1, 1)

        self.label_25 = QLabel(self.ram_info_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 37))
        self.label_25.setMaximumSize(QSize(90, 50))
        self.label_25.setFont(font8)

        self.gridLayout_2.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_19 = QLabel(self.ram_info_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 37))
        self.label_19.setMaximumSize(QSize(90, 50))
        self.label_19.setFont(font8)

        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 1)

        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")
        self.total_ram.setMinimumSize(QSize(95, 37))
        self.total_ram.setMaximumSize(QSize(95, 50))
        self.total_ram.setFont(font9)
        self.total_ram.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.total_ram, 0, 1, 1, 1)

        self.available_ram = QLabel(self.ram_info_frame)
        self.available_ram.setObjectName(u"available_ram")
        self.available_ram.setMinimumSize(QSize(95, 37))
        self.available_ram.setMaximumSize(QSize(95, 50))
        self.available_ram.setFont(font9)
        self.available_ram.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.available_ram, 1, 1, 1, 1)

        self.label_23 = QLabel(self.ram_info_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 37))
        self.label_23.setMaximumSize(QSize(90, 50))
        self.label_23.setFont(font8)

        self.gridLayout_2.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_21 = QLabel(self.ram_info_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 37))
        self.label_21.setMaximumSize(QSize(90, 50))
        self.label_21.setFont(font8)

        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)

        self.free_ram = QLabel(self.ram_info_frame)
        self.free_ram.setObjectName(u"free_ram")
        self.free_ram.setMinimumSize(QSize(95, 37))
        self.free_ram.setMaximumSize(QSize(95, 50))
        self.free_ram.setFont(font9)
        self.free_ram.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.free_ram, 3, 1, 1, 1)

        self.ram_percantage = spiralProgressBar(self.ram_info_frame)
        self.ram_percantage.setObjectName(u"ram_percantage")
        self.ram_percantage.setMinimumSize(QSize(155, 155))
        self.ram_percantage.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.ram_percantage, 0, 2, 5, 1)


        self.verticalLayout_7.addWidget(self.ram_info_frame)


        self.horizontalLayout_12.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.mainFrame)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"#widget_5{\n"
"background-color: #e0ffee;\n"
"border-radius: 28px;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.widget_5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.widget_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"     height: 30px;\n"
"     width: 150px;\n"
"     color: #000;\n"
"     background-color: #e0ffee;\n"
"}\n"
"QCalendarWidget QMenu {\n"
"     left: 0px;\n"
"     color: #fff;\n"
"     font-size: 18px;\n"
"     background-color:  #fff;\n"
"}\n"
"QCalendarWidget QSpinBox { \n"
"     color:  #000; \n"
"     background-color: #fff; \n"
"     selection-background-color: rgb(136, 136, 136);\n"
"     selection-color:  #000;\n"
"}\n"
"QCalendarWidget QSpinBox::up-button { \n"
"  subcontrol-origin: border;  \n"
"  subcontrol-position: top right;  \n"
"  width:15px;\n"
"}\n"
"QCalendarWidget QSpinBox::down-button {\n"
"  subcontrol-origin: border; \n"
"  subcontrol-position: bottom right;  \n"
"  width:15px;\n"
"}\n"
"QCalendarWidget QSpinBox::up-arrow { \n"
"  width:10px;  \n"
"  height:10px; \n"
"}\n"
"QCalendarWidget QSpinBox::down-arrow { \n"
"  width:10px;  \n"
"  height:10px; \n"
"}\n"
"   \n"
"  /* header row */\n"
"QCalendarWidget QWidget {\n"
" alternate-background-color: #f5f"
                        "8ff; \n"
"}\n"
"   \n"
"  /* normal days */\n"
"QCalendarWidget QAbstractItemView:enabled \n"
"{\n"
"     color: #2596be;  \n"
"     background-color: #fffbfb;  \n"
"     selection-background-color:#b2e5c1; \n"
"     selection-color: #fff; \n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"  color: rgb(64, 64, 64); \n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.calendarWidget = QCalendarWidget(self.frame_8)
        self.calendarWidget.setObjectName(u"calendarWidget")
        font10 = QFont()
        font10.setFamily(u"Calibri")
        font10.setPointSize(13)
        self.calendarWidget.setFont(font10)

        self.horizontalLayout_15.addWidget(self.calendarWidget)


        self.verticalLayout_14.addWidget(self.frame_8)


        self.horizontalLayout_12.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.mainFrame)


        self.horizontalLayout_18.addWidget(self.mainBody)

        self.profCont = QCustomSlideMenu(self.homePage)
        self.profCont.setObjectName(u"profCont")
        self.profCont.setMinimumSize(QSize(0, 0))
        self.profCont.setMaximumSize(QSize(130, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.profCont)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 0)
        self.frame_15 = QFrame(self.profCont)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setSpacing(8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 8, 0, 0)
        self.label_49 = QLabel(self.frame_15)
        self.label_49.setObjectName(u"label_49")
        font11 = QFont()
        font11.setFamily(u"\u5b8b\u4f53")
        font11.setPointSize(13)
        font11.setBold(True)
        font11.setWeight(75)
        self.label_49.setFont(font11)
        self.label_49.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_49, 0, Qt.AlignTop)

        self.label_50 = QLabel(self.frame_15)
        self.label_50.setObjectName(u"label_50")
        font12 = QFont()
        font12.setFamily(u"\u5b8b\u4f53")
        font12.setPointSize(13)
        self.label_50.setFont(font12)
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_50, 0, Qt.AlignTop)

        self.label_51 = QLabel(self.frame_15)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(50, 50))
        self.label_51.setMaximumSize(QSize(50, 50))
        self.label_51.setFont(font12)
        self.label_51.setPixmap(QPixmap(u":/icons/user.png"))
        self.label_51.setScaledContents(True)
        self.label_51.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_51, 0, Qt.AlignHCenter)

        self.pushButton_7 = QPushButton(self.frame_15)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon8 = QIcon()
        icon8.addFile(u":/icons/info2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)

        self.verticalLayout_13.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_15)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon9 = QIcon()
        icon9.addFile(u":/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon9)

        self.verticalLayout_13.addWidget(self.pushButton_8)


        self.verticalLayout_10.addWidget(self.frame_15, 0, Qt.AlignTop)


        self.horizontalLayout_18.addWidget(self.profCont, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.homePage)
        self.ocrPage = QWidget()
        self.ocrPage.setObjectName(u"ocrPage")
        self.ocrPage.setMouseTracking(True)
        self.ocrPage.setStyleSheet(u"QLineEdit{\n"
"	background: transparent;\n"
"	color: #25a1be;\n"
"}\n"
"#searchFrame,#openBtn{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"#ocrPage{\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(157, 195, 231, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"#ocrPage{\n"
"	font: 9pt \"\u5b8b\u4f53\";\n"
"}\n"
"\n"
"#loadWidget {\n"
"	background-color: #fefeff;\n"
"	border-top-left-radius: 20px ;\n"
"	border-top-right-radius: 20px \n"
"}\n"
"#labelName{\n"
"border-bottom: 3px dashed rgb(157, 195, 231);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	width: 16px;\n"
"	height: 16px;\n"
"}\n"
" \n"
" \n"
"QRadioButton::indicator::unchecked {\n"
"	image: url(:/icons/radio_uncheck.png);\n"
"}\n"
" \n"
"QRadioButton::indicator::unchecked:hover {\n"
"	image: url(:/icons/radio_hover.png);\n"
"}\n"
" \n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/icons/radio_checked.png);\n"
"}\n"
"#processBtn{\n"
"	background-position:HCenter;\n"
"	text-align:left\n"
"}"
                        "\n"
"\n"
"QPushButton{\n"
"font-family:\"\u4eff\u5b8b\"\n"
"font-weight:bold\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_15 = QVBoxLayout(self.ocrPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.ocrWidget = QWidget(self.ocrPage)
        self.ocrWidget.setObjectName(u"ocrWidget")
        sizePolicy.setHeightForWidth(self.ocrWidget.sizePolicy().hasHeightForWidth())
        self.ocrWidget.setSizePolicy(sizePolicy)
        self.ocrWidget.setMinimumSize(QSize(0, 500))
        self.verticalLayout = QVBoxLayout(self.ocrWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchFile = QWidget(self.ocrWidget)
        self.searchFile.setObjectName(u"searchFile")
        sizePolicy.setHeightForWidth(self.searchFile.sizePolicy().hasHeightForWidth())
        self.searchFile.setSizePolicy(sizePolicy)
        self.searchFile.setMaximumSize(QSize(16777215, 300))
        self.horizontalLayout_4 = QHBoxLayout(self.searchFile)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.searchFrame = QWidget(self.searchFile)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(500, 40))
        self.searchFrame.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.label_2 = QLabel(self.searchFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/icons/search.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.lineEdit = MLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(30, 30))
        font13 = QFont()
        font13.setFamily(u"Lucida Bright")
        font13.setPointSize(12)
        self.lineEdit.setFont(font13)

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_4.addWidget(self.searchFrame)

        self.openBtn = QPushButton(self.searchFile)
        self.openBtn.setObjectName(u"openBtn")
        self.openBtn.setMinimumSize(QSize(70, 50))
        self.openBtn.setMaximumSize(QSize(70, 50))
        icon10 = QIcon()
        icon10.addFile(u":/icons/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openBtn.setIcon(icon10)
        self.openBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.openBtn)


        self.verticalLayout.addWidget(self.searchFile, 0, Qt.AlignTop)

        self.buttonWidget = QWidget(self.ocrWidget)
        self.buttonWidget.setObjectName(u"buttonWidget")
        self.buttonWidget.setMinimumSize(QSize(0, 50))
        self.buttonWidget.setMaximumSize(QSize(16777215, 40))
        self.buttonWidget.setStyleSheet(u"#buttonWidget{\n"
"border-bottom: 3px dashed rgb(55, 195, 167);\n"
"}")
        self.GPUBtn = QRadioButton(self.buttonWidget)
        self.GPUBtn.setObjectName(u"GPUBtn")
        self.GPUBtn.setGeometry(QRect(630, 10, 71, 16))
        self.GPUBtn.setMaximumSize(QSize(100, 16777215))
        font14 = QFont()
        font14.setFamily(u"\u5b8b\u4f53")
        font14.setPointSize(10)
        font14.setBold(True)
        font14.setWeight(75)
        self.GPUBtn.setFont(font14)
        self.GPUBtn.setIconSize(QSize(32, 32))
        self.processBtn = QPushButton(self.buttonWidget)
        self.processBtn.setObjectName(u"processBtn")
        self.processBtn.setGeometry(QRect(750, 0, 150, 32))
        self.processBtn.setMinimumSize(QSize(50, 0))
        self.processBtn.setMaximumSize(QSize(150, 16777215))
        self.processBtn.setFont(font14)
        icon11 = QIcon()
        icon11.addFile(u":/icons/doOcr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.processBtn.setIcon(icon11)
        self.processBtn.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.buttonWidget)

        self.processWidget = QWidget(self.ocrWidget)
        self.processWidget.setObjectName(u"processWidget")
        self.processWidget.setMinimumSize(QSize(0, 390))
        self.processWidget.setMaximumSize(QSize(8888, 16777215))
        self.processWidget.setMouseTracking(False)
        self.processWidget.setStyleSheet(u"")
        self.horizontalLayout_20 = QHBoxLayout(self.processWidget)
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(5, 0, 0, 0)
        self.loadWidget = QWidget(self.processWidget)
        self.loadWidget.setObjectName(u"loadWidget")
        self.loadWidget.setMinimumSize(QSize(150, 330))
        self.loadWidget.setMaximumSize(QSize(140, 300))
        self.verticalLayout_16 = QVBoxLayout(self.loadWidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(2, 2, 2, 0)
        self.labelName = QLabel(self.loadWidget)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setMinimumSize(QSize(150, 20))
        self.labelName.setMaximumSize(QSize(150, 16777215))
        font15 = QFont()
        font15.setFamily(u"\u5b8b\u4f53")
        font15.setPointSize(12)
        self.labelName.setFont(font15)
        self.labelName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.labelName, 0, Qt.AlignHCenter)

        self.loadLabel = QLabel(self.loadWidget)
        self.loadLabel.setObjectName(u"loadLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.loadLabel.sizePolicy().hasHeightForWidth())
        self.loadLabel.setSizePolicy(sizePolicy6)
        self.loadLabel.setMinimumSize(QSize(133, 293))
        self.loadLabel.setMaximumSize(QSize(150, 293))
        self.loadLabel.setSizeIncrement(QSize(0, 0))
        self.loadLabel.setLayoutDirection(Qt.LeftToRight)
        self.loadLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.loadLabel, 0, Qt.AlignBottom)


        self.horizontalLayout_20.addWidget(self.loadWidget, 0, Qt.AlignVCenter)

        self.progress = FormProgressIndicator(self.processWidget)
        self.progress.setObjectName(u"progress")
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setMinimumSize(QSize(160, 750))
        self.progress.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_20.addWidget(self.progress, 0, Qt.AlignVCenter)

        self.listWidget = QWidget(self.processWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"/*\n"
"tabelwidget*/\n"
"QTableWidget{\n"
"color:#809fff;\n"
"background:#f6f3fa;\n"
"border:1px solid #242424;\n"
"alternate-background-color:#66b2ff;/*\u4ea4\u9519\u989c\u8272*/\n"
"gridline-color:#242424;\n"
"}\n"
"QListWidget::Item{\n"
"color=#000000\n"
"\n"
"}\n"
"\n"
"\n"
"/*\u9009\u4e2ditem*/\n"
"QTableWidget::item:selected{\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(77, 120, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"/*\n"
"\u60ac\u6d6eitem*/\n"
"QTableWidget::item:hover{\n"
"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(128, 159, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"/*\u8868\u5934*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"background:#809fff;\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#DCDCDC;\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"\n"
"\n"
"/*\u8868\u53f3\u4fa7\u7684\u6ed1\u6761*/\n"
"QScrollBar:vertical{\n"
"background:#99ccff;\n"
"padding:"
                        "0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"/*\u6ed1\u5757*/\n"
"QScrollBar:horizontal{\n"
"border-radius:6px;\n"
"background:#99ccff;\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:#A7A7A7;\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u5df2\u7ecf\u5212\u8fc7\u7684\u533a\u57df*/\n"
"QScrollBar::sub-page:vertical{\n"
"background:444444;\n"
"}\n"
"\n"
"/*\n"
"\u6ed1\u5757\u8fd8\u6ca1\u6709\u5212\u8fc7\u7684\u533a\u57df*/\n"
"QScrollBar::add-page:vertical{\n"
"background:5B5B5B;\n"
"}\n"
"\n"
"/*\u9875\u9762\u4e0b\u79fb\u7684\u6309\u94ae*/\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"/*\u9875\u9762\u4e0a\u79fb\u7684\u6309\u94ae*/\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.listWidget)
        self.verticalLayout_17.setSpacing(4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.listWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: #ffff;\n"
"	border-radius: 10px;\n"
"	border: 2px #000\n"
"}")
        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        icon12 = QIcon()
        icon12.addFile(u":/icons/color.png", QSize(), QIcon.Normal, QIcon.Off)
        font16 = QFont()
        font16.setFamily(u"\u65b0\u5b8b\u4f53")
        font16.setBold(True)
        font16.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font16);
        __qtablewidgetitem.setIcon(icon12);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon13 = QIcon()
        icon13.addFile(u":/icons/tele.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font8);
        __qtablewidgetitem1.setBackground(QColor(0, 0, 0));
        __qtablewidgetitem1.setIcon(icon13);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon14 = QIcon()
        icon14.addFile(u":/icons/day.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font16);
        __qtablewidgetitem2.setIcon(icon14);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon15 = QIcon()
        icon15.addFile(u":/icons/time.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font16);
        __qtablewidgetitem3.setIcon(icon15);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        icon16 = QIcon()
        icon16.addFile(u":/icons/place.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font16);
        __qtablewidgetitem4.setIcon(icon16);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 40, 601, 318))
        self.tableWidget.setMaximumSize(QSize(1000, 16777215))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.listBtn = QWidget(self.widget_2)
        self.listBtn.setObjectName(u"listBtn")
        self.listBtn.setGeometry(QRect(0, 0, 621, 31))
        sizePolicy.setHeightForWidth(self.listBtn.sizePolicy().hasHeightForWidth())
        self.listBtn.setSizePolicy(sizePolicy)
        self.listBtn.setStyleSheet(u"#clearBtn,#delBtn{\n"
"background-color: #afbfff;\n"
"	color: #fff;\n"
"	border-radius: 10px;\n"
"}\n"
"#uploadBtn{\n"
"background-color: #f5b38e;\n"
"	color: #fff;\n"
"	border-radius: 10px;\n"
"}")
        self.uploadBtn = QPushButton(self.listBtn)
        self.uploadBtn.setObjectName(u"uploadBtn")
        self.uploadBtn.setGeometry(QRect(490, 0, 121, 31))
        font17 = QFont()
        font17.setFamily(u"\u65b0\u5b8b\u4f53")
        font17.setPointSize(10)
        font17.setBold(True)
        font17.setWeight(75)
        self.uploadBtn.setFont(font17)
        icon17 = QIcon()
        icon17.addFile(u":/icons/database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.uploadBtn.setIcon(icon17)
        self.uploadBtn.setIconSize(QSize(32, 32))
        self.clearBtn = QPushButton(self.listBtn)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setGeometry(QRect(380, 0, 101, 31))
        self.clearBtn.setFont(font14)
        icon18 = QIcon()
        icon18.addFile(u":/icons/reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearBtn.setIcon(icon18)
        self.clearBtn.setIconSize(QSize(30, 30))
        self.delBtn = QPushButton(self.listBtn)
        self.delBtn.setObjectName(u"delBtn")
        self.delBtn.setGeometry(QRect(250, 0, 121, 31))
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.delBtn.sizePolicy().hasHeightForWidth())
        self.delBtn.setSizePolicy(sizePolicy7)
        self.delBtn.setMaximumSize(QSize(16777215, 80))
        self.delBtn.setFont(font14)
        icon19 = QIcon()
        icon19.addFile(u":/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delBtn.setIcon(icon19)
        self.delBtn.setIconSize(QSize(36, 36))
        self.delBtn.setFlat(True)

        self.verticalLayout_17.addWidget(self.widget_2)


        self.horizontalLayout_20.addWidget(self.listWidget)


        self.verticalLayout.addWidget(self.processWidget, 0, Qt.AlignVCenter)


        self.verticalLayout_15.addWidget(self.ocrWidget)

        self.stackedWidget.addWidget(self.ocrPage)
        self.percentPage = QWidget()
        self.percentPage.setObjectName(u"percentPage")
        self.percentPage.setStyleSheet(u"#percentPage{\n"
"background-color: rgb(33, 43, 51);\n"
"}\n"
"\n"
"")
        self.percentage_bar_chart = QWidget(self.percentPage)
        self.percentage_bar_chart.setObjectName(u"percentage_bar_chart")
        self.percentage_bar_chart.setGeometry(QRect(0, 0, 950, 565))
        self.percentage_bar_chart.setMinimumSize(QSize(950, 550))
        self.percentage_bar_chart.setMaximumSize(QSize(590, 8888))
        self.percentage_bar_chart.setStyleSheet(u"*{\n"
"background-color: rgb(33, 43, 51);\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.percentage_bar_chart)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.percentage_bar_chart)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setMinimumSize(QSize(950, 550))
        self.frame_16.setMaximumSize(QSize(950, 1000))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.percentage_bar_chart_cont = QGridLayout(self.frame_16)
        self.percentage_bar_chart_cont.setObjectName(u"percentage_bar_chart_cont")
        self.percentage_bar_chart_cont.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_18.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.percentPage)
        self.barPage = QWidget()
        self.barPage.setObjectName(u"barPage")
        self.barPage.setStyleSheet(u"#barPage{\n"
"background-color: rgb(33, 43, 51);\n"
"}\n"
"\n"
"")
        self.bar_charts = QWidget(self.barPage)
        self.bar_charts.setObjectName(u"bar_charts")
        self.bar_charts.setGeometry(QRect(0, 0, 950, 565))
        self.bar_charts.setMinimumSize(QSize(950, 550))
        self.bar_charts.setMaximumSize(QSize(590, 8888))
        self.bar_charts.setStyleSheet(u"*{\n"
"background-color: rgb(33, 43, 51);\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.bar_charts)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.bar_charts)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setMinimumSize(QSize(950, 550))
        self.frame_17.setMaximumSize(QSize(950, 1000))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.bar_charts_cont = QGridLayout(self.frame_17)
        self.bar_charts_cont.setObjectName(u"bar_charts_cont")
        self.bar_charts_cont.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_19.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.barPage)
        self.piePage = QWidget()
        self.piePage.setObjectName(u"piePage")
        self.piePage.setStyleSheet(u"#piePage{\n"
"background-color: rgb(33, 43, 51);\n"
"}\n"
"\n"
"")
        self.pie_charts = QWidget(self.piePage)
        self.pie_charts.setObjectName(u"pie_charts")
        self.pie_charts.setGeometry(QRect(0, 0, 950, 527))
        self.pie_charts.setStyleSheet(u"*{\n"
"background-color: rgb(33, 43, 51);\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.pie_charts)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.pie_charts)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QSize(950, 527))
        self.frame_18.setMaximumSize(QSize(950, 527))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.nested_donut_chart_cont = QGridLayout(self.frame_18)
        self.nested_donut_chart_cont.setObjectName(u"nested_donut_chart_cont")
        self.nested_donut_chart_cont.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_20.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.piePage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"OpenCV LAB", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.ocrBtn.setText(QCoreApplication.translate("MainWindow", u"\u884c\u7a0b\u5361\u8bc6\u522b", None))
        self.percentBtn.setText(QCoreApplication.translate("MainWindow", u"\u767e\u5206\u6bd4\u67f1\u5f62\u56fe", None))
        self.barBtn.setText(QCoreApplication.translate("MainWindow", u"\u6761\u5f62\u6298\u7ebf\u56fe", None))
        self.pieBtn.setText(QCoreApplication.translate("MainWindow", u"\u5d4c\u5957\u5f62\u997c\u56fe", None))
        self.menuBtn.setText("")
        self.appHeader.setText(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
        self.label_3.setText("")
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"www.cqu.edu.cn", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6587\u4ef6\u8def\u5f84", None))
        self.accountBtn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u5e86\u5927\u5b66\u5c0f\u5b66\u671f\u5b9e\u8bad\u9879\u76ee", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4e86\u89e3\u66f4\u591a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CPU \u5229\u7528\u7387", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CPU \u5185\u6838", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"CPU \u903b\u8f91\u5904\u7406\u5668", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u7a7a\u95f2\u7269\u7406\u5185\u5b58", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u603b\u7684\u7269\u7406\u5185\u5b58", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u7528\u7269\u7406\u5185\u5b58", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u7528\u7269\u7406\u5185\u5b58", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u66fe\u9889", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u5458", None))
        self.label_51.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.label_2.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6587\u4ef6\u8def\u5f84", None))
        self.openBtn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.GPUBtn.setText(QCoreApplication.translate("MainWindow", u"GPU\u52a0\u901f", None))
        self.processBtn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5904\u7406", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5904\u7406\u533a", None))
        self.loadLabel.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u884c\u7a0b\u7801\u989c\u8272", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8bdd", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u884c\u7a0b", None));
        self.uploadBtn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u6570\u636e\u5e93", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8868\u5355", None))
        self.delBtn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u4e2d\u884c", None))
    # retranslateUi

