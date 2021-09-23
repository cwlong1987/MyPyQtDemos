#### 说明一
对比 [QWebEngineView使用模板1](https://www.jianshu.com/p/5f6e29a357f1)，抛弃了创建新窗口的实现方法。
而是使用QTabWidget，创建新的tab来实现，这样更加符合浏览器的设计。

#### 说明二
QWebEngineView，结合 QTabWidget ，模拟了常规浏览器的简单实现。
本例依旧十分简陋，很多功能并没有进行扩展开发。
抛砖引玉，希望对大家有所帮助。

#### 效果图
![](https://upload-images.jianshu.io/upload_images/1724251-4ce2f14a14ce80d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




【如下代码，完全复制，直接运行，即可使用】
```python
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Browser')
        self.showMaximized()
        self.setWindowFlags(Qt.FramelessWindowHint)

        #####创建tabwidget
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)
        self.setCentralWidget(self.tabWidget)

        ####第一个tab
        self.webview = WebEngineView(self)   #self必须要有，是将主窗口作为参数，传给浏览器
        self.webview.load(QUrl("http://www.baidu.com"))
        self.create_tab(self.webview)


    #创建tab
    def create_tab(self,webview):
        self.tab = QWidget()
        self.tabWidget.addTab(self.tab, "新标签页")
        self.tabWidget.setCurrentWidget(self.tab)
        #####
        self.Layout = QHBoxLayout(self.tab)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addWidget(webview)



    #关闭tab
    def close_Tab(self,index):
        if self.tabWidget.count()>1:
            self.tabWidget.removeTab(index)
        else:
            self.close()   # 当只有1个tab时，关闭主窗口





################################################
#######创建浏览器
################################################
class WebEngineView(QWebEngineView):

    def __init__(self,mainwindow,parent=None):
        super(WebEngineView, self).__init__(parent)
        self.mainwindow = mainwindow


    # 重写createwindow()
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView(self.mainwindow)

        self.mainwindow.create_tab(new_webview)

        return new_webview


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = MainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())
```
本文如有帮助，敬请留言鼓励。
本文如有错误，敬请留言改进。