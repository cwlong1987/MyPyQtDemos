####说明1：关于QWebEngineView
pyqt5 已经抛弃  QtWebKit和QtWebKitWidgets，而使用最新的QtWebEngineWidgets。
QtWebEngineWidgets，是基于chrome浏览器内核引擎的。


####说明2：关于左键点击页面跳转
其中，最让纠结的就是实现左键点击页面跳转了。
在chrome浏览器上，有些页面，左键点击，会直接创建一个新的tab来呈现网页。
在使用QWebEngineView时，如果不做特殊处理，这样的左键点击，是根本没有反应的。
那怎么办？就需要重写QWebEngineView的createWindow方法。

####说明3：关于createWindow方法重写
在重写QWebEngineView的createWindow方法时，又有两种写法。
**第一种**，是直接在本窗口新建tab的方式。   （不推荐使用这种方式）
注：这种方式有个问题，因为新建的tab覆盖了原来的tab，所以，原来tab的所有信息都找不到了，如浏览，账号，密码等。
```python
class WebEngineView(QWebEngineView):
    # 重写createwindow()
    def createWindow(self, QWebEnginePage_WebWindowType):
        return self
```



**第二种**，就是新建窗口的方式了。代码如下。（推荐使用这种方式）


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

        self.webview = WebEngineView()
        self.webview.load(QUrl("https://www.baidu.com"))
        self.setCentralWidget(self.webview)




################################################
#######创建浏览器
################################################
class WebEngineView(QWebEngineView):
    windowList = []

    # 重写createwindow()
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview =   WebEngineView()
        new_window = MainWindow()
        new_window.setCentralWidget(new_webview)
        #new_window.show()
        self.windowList.append(new_window)  #注：没有这句会崩溃！！！
        return new_webview


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


```



本文如有帮助，敬请留言鼓励。
本文如有错误，敬请留言改进。