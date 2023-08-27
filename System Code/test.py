# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(902, 891)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 2, 536, 574))
        self._2 = QVBoxLayout(self.layoutWidget)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 158, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self._2.addItem(self.verticalSpacer)

        self._4 = QHBoxLayout()
        self._4.setObjectName(u"_4")
        self.horizontalSpacer = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._4.addItem(self.horizontalSpacer)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self._4.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._4.addItem(self.horizontalSpacer_2)


        self._2.addLayout(self._4)

        self._3 = QHBoxLayout()
        self._3.setObjectName(u"_3")
        self.horizontalSpacer_3 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._3.addItem(self.horizontalSpacer_3)

        self.input1 = QDoubleSpinBox(self.layoutWidget)
        self.input1.setObjectName(u"input1")

        self._3.addWidget(self.input1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self._3.addWidget(self.label_2)

        self.input2 = QDoubleSpinBox(self.layoutWidget)
        self.input2.setObjectName(u"input2")

        self._3.addWidget(self.input2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self._3.addWidget(self.label_3)

        self.result = QLabel(self.layoutWidget)
        self.result.setObjectName(u"result")

        self._3.addWidget(self.result)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._3.addItem(self.horizontalSpacer_4)


        self._2.addLayout(self._3)

        self._5 = QHBoxLayout()
        self._5.setObjectName(u"_5")
        self.horizontalSpacer_5 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._5.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self._5.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.layoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self._5.addWidget(self.progressBar)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._5.addItem(self.horizontalSpacer_6)


        self._2.addLayout(self._5)

        self._6 = QHBoxLayout()
        self._6.setObjectName(u"_6")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._6.addItem(self.horizontalSpacer_7)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self._6.addWidget(self.label_5)

        self.timeCost = QSpinBox(self.layoutWidget)
        self.timeCost.setObjectName(u"timeCost")

        self._6.addWidget(self.timeCost)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self._6.addWidget(self.pushButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self._6.addItem(self.horizontalSpacer_8)


        self._2.addLayout(self._6)

        self.verticalSpacer_2 = QSpacerItem(20, 168, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self._2.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 902, 45))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u6cd5\u5668", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"\uff1f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5ea6", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u65f6", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
    # retranslateUi

