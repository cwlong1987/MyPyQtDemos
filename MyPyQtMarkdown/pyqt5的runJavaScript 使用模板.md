#### runJavaScript 的说明
QWebEnginePage  有一个 runJavaScript 方法，支持回调函数。

**使用方法1**
只运行JavaScript，没有回调
```python
   def run_js(self):
        js_string = '''
        alert("hello,world！");
        '''

        self.webview.page().runJavaScript(js_string)
```

**使用方法2**
运行JavaScript，并存在回调
```python
    def run_js2(self):
        js_string = '''
        function myFunction()
        {
            return document.body.scrollWidth;
        }
                
        myFunction();
        '''

        self.webview.page().runJavaScript(js_string , self.js_callback)



    # 回调函数
    def js_callback(self,result):
        print(result)
        QMessageBox.information(self, "提示", str(result))

```
完整代码，如下所示。


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

        #####放入WebEngineView
        self.webview = WebEngineView()
        self.webview.load(QUrl("https://www.baidu.com"))
        self.setCentralWidget(self.webview)

        #####web页面加载完毕，调用函数
        self.webview.page().loadFinished.connect(self.run_js)
        self.webview.page().loadFinished.connect(self.run_js2)



    ########运行js脚本，没有回调########
    def run_js(self):
        js_string = '''
        alert("hello,world！");
        '''

        self.webview.page().runJavaScript(js_string)


    ########运行js脚本，有回调########
    def run_js2(self):
        js_string = '''
        function myFunction()
        {
            return document.body.scrollWidth;
        }
                
        myFunction();
        '''

        self.webview.page().runJavaScript(js_string , self.js_callback)



    # 回调函数
    def js_callback(self,result):
        print(result)
        QMessageBox.information(self, "提示", str(result))


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
        self.windowList.append(new_window)  #注：没有这句会崩溃
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