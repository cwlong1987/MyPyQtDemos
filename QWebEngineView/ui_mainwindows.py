# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindows.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 753)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_forward = QtWidgets.QPushButton(self.frame2)
        self.pushButton_forward.setObjectName("pushButton_forward")
        self.horizontalLayout.addWidget(self.pushButton_forward)
        self.pushButton_back = QtWidgets.QPushButton(self.frame2)
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.pushButton_refresh = QtWidgets.QPushButton(self.frame2)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout.addWidget(self.pushButton_refresh)
        self.pushButton_homepage = QtWidgets.QPushButton(self.frame2)
        self.pushButton_homepage.setObjectName("pushButton_homepage")
        self.horizontalLayout.addWidget(self.pushButton_homepage)
        self.lineEdit_url = QtWidgets.QLineEdit(self.frame2)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.verticalLayout.addWidget(self.frame2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_forward.setText(_translate("MainWindow", "前进"))
        self.pushButton_back.setText(_translate("MainWindow", "后退"))
        self.pushButton_refresh.setText(_translate("MainWindow", "刷新"))
        self.pushButton_homepage.setText(_translate("MainWindow", "主页"))

