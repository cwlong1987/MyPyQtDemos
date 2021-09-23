
from QWebEngineView.ui_mainwindows import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QMainWindow,QWidget
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
####################################
#主界面
####################################
class mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainwindow,self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()

        self.lineEdit_url.returnPressed.connect(self.on_pushButton_go_clicked)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)

        self.webview = WebEngineView()
        self.webview.load(QUrl("http://www.baidu.com"))
        self.create_tab(self.webview)



    def close_Tab(self,index):
        if self.tabWidget.count()>1:
            self.tabWidget.removeTab(index)




    def create_tab(self,webview):
        self.tab = QWidget()
        self.tabWidget.addTab(self.tab, "新标签页")

        #####
        self.Layout = QHBoxLayout(self.tab)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addWidget(webview)
        #####
        self.tabWidget.setCurrentWidget(self.tab)
        #####
        #self.webview = webview
        #self.webview.page().loadFinished.connect(self.set_tab_title)
        #self.webview.urlChanged.connect(self.renew_urlbar)



    def set_tab_title(self):
        pass
        #the_title = self.webview.page().title()
        #self.tabWidget.setTabText(self.tabWidget.currentIndex(),the_title)

        #the_icon = self.webview.page().icon()
        #self.tabWidget.setTabIcon(self.tabWidget.currentIndex(),the_icon)


    #刷新地址栏
    def renew_urlbar(self, qurl):

        self.lineEdit_url.setText(qurl.url())
        self.lineEdit_url.setCursorPosition(0)
        self.renew_pushButton()




    # 浏览按钮
    @pyqtSlot()
    def on_pushButton_go_clicked(self):
        if self.lineEdit_url.text() !="":
            url = QUrl(self.lineEdit_url.text())
            self.webview.load(url)



    #刷新按钮
    @pyqtSlot()
    def on_pushButton_refresh_clicked(self):
        self.webview.reload()


    #主页按钮
    @pyqtSlot()
    def on_pushButton_homepage_clicked(self):
        self.homepage_url = "http://www.baidu.com"
        url = QUrl(self.homepage_url)
        self.webview.load(url)

    #回退按钮
    @pyqtSlot()
    def on_pushButton_back_clicked(self):
        page = self.webview.page()
        history = page.history()
        #history = self.webview.history()
        history.back()
        self.renew_pushButton()


    #前进按钮
    @pyqtSlot()
    def on_pushButton_forward_clicked(self):
        page = self.webview.page()
        history = page.history()
        #history = self.webview.history()
        history.forward()
        self.renew_pushButton()


    # 打开网页
    def open_web(self,url):
        if url.scheme() == '':
            url.setScheme('https')
        self.webview.setUrl(url)






    #刷新按钮
    def renew_pushButton(self):
        page = self.webview.page()
        history = page.history()
        #history =self.webview.history()
        if history.canGoBack():
            self.pushButton_back.setEnabled(True)
        else:
            self.pushButton_back.setEnabled(False)

        if history.canGoForward():
            self.pushButton_forward.setEnabled(True)
        else:
            self.pushButton_forward.setEnabled(False)

################################################
#######创建浏览器
################################################
class WebEngineView(QWebEngineView):

    # 重写createwindow()
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView()

        theshow.create_tab(new_webview)

        return new_webview


####################################
#程序入口
####################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    theshow = mainwindow()
    theshow.show()
    sys.exit(app.exec_())