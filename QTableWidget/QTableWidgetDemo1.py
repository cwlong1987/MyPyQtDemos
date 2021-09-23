import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('主界面')

        ###### 创建界面 ######
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.Layout = QVBoxLayout(self.centralwidget)

        # 设置QTableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableWidget.setColumnCount(23)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(True)

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)


        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("内部编号")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("快递单号")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("寄件单位名称")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("寄件人姓名")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("寄件人手机")
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText("寄件人地址")
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText("收件单位名称")
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText("收件人姓名")
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText("收件人电话")


        self.Layout.addWidget(self.tableWidget)




        # 设置状态栏
        self.statusBar().showMessage("当前用户：一心狮")

        # 窗口最大化
        self.showMaximized()

        # 获取数据，并显示数据
        self.goto_getdata()







    # 获取数据
    def goto_getdata(self):
        the_datas={

        }



################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = MainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())