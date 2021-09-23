from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox

import sys

from MainWindowDemos.ui_uidemo1 import Ui_UIDemo1
from PyQt5.QtCore import Qt
####################################
#主界面
####################################
class mainwindow(QtWidgets.QDialog, Ui_UIDemo1):
    def __init__(self, parent=None):
        super(mainwindow,self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.setWindowFlags(Qt.FramelessWindowHint)



####################################
#程序入口
####################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    theshow = mainwindow()
    theshow.show()
    sys.exit(app.exec_())