### 相关说明
使用QCompleter类，就可以实现自动补全功能，效果图如下：
![](https://upload-images.jianshu.io/upload_images/1724251-db91fea7710d958d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![](https://upload-images.jianshu.io/upload_images/1724251-3232cc17e3c861ea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

对应的代码很简单
```python
    def init_lineedit(self):
        # 增加自动补全
        self.completer = QCompleter(items_list)
        # 设置匹配模式  有三种： Qt.MatchStartsWith 开头匹配（默认）  Qt.MatchContains 内容匹配  Qt.MatchEndsWith 结尾匹配
        self.completer.setFilterMode(Qt.MatchContains)
        # 设置补全模式  有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
        self.completer.setCompletionMode(QCompleter.PopupCompletion) 
        # 给lineedit设置补全器
        self.lineedit.setCompleter(self.completer)


    def init_combobox(self):
        # 增加选项元素
        for i in range(len(items_list)):
            self.combobox.addItem(items_list[i])
        self.combobox.setCurrentIndex(-1)

        # 增加自动补全
        self.completer = QCompleter(items_list)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.combobox.setCompleter(self.completer)
```



【如下代码，完全复制，直接运行，即可使用】
```python
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
################################################

items_list=["C","C++","Java","Python","JavaScript","C#","Swift","go","Ruby","Lua","PHP"]

################################################
class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        self.lineedit = QLineEdit(self, minimumWidth=200)
        self.combobox = QComboBox(self, minimumWidth=200)
        self.combobox.setEditable(True)


        layout.addWidget(QLabel("QLineEdit", self))
        layout.addWidget(self.lineedit)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        layout.addWidget(QLabel("QComboBox", self))
        layout.addWidget(self.combobox)


        #初始化combobox
        self.init_lineedit()
        self.init_combobox()


        #增加选中事件
        self.combobox.activated.connect(self.on_combobox_Activate)



    def init_lineedit(self):
        # 增加自动补全
        self.completer = QCompleter(items_list)
        # 设置匹配模式  有三种： Qt.MatchStartsWith 开头匹配（默认）  Qt.MatchContains 内容匹配  Qt.MatchEndsWith 结尾匹配
        self.completer.setFilterMode(Qt.MatchContains)
        # 设置补全模式  有三种： QCompleter.PopupCompletion（默认）  QCompleter.InlineCompletion   QCompleter.UnfilteredPopupCompletion
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        # 给lineedit设置补全器
        self.lineedit.setCompleter(self.completer)



    def init_combobox(self):
        # 增加选项元素
        for i in range(len(items_list)):
            self.combobox.addItem(items_list[i])
        self.combobox.setCurrentIndex(-1)

        # 增加自动补全
        self.completer = QCompleter(items_list)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.combobox.setCompleter(self.completer)


    def on_combobox_Activate(self, index):
        print(self.combobox.count())
        print(self.combobox.currentIndex())
        print(self.combobox.currentText())
        print(self.combobox.currentData())
        print(self.combobox.itemData(self.combobox.currentIndex()))
        print(self.combobox.itemText(self.combobox.currentIndex()))
        print(self.combobox.itemText(index))






if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
```
本文如有帮助，敬请留言鼓励。
本文如有错误，敬请留言改进。