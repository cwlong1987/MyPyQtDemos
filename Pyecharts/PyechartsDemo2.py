import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

from pyecharts.charts import Line
from pyecharts import options
################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Browser')
        self.showMaximized()

        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)
        ###############################################
        self.goto_creat_pyecharts()



    def goto_creat_pyecharts(self):
        ######################################################
        the_abscissa_list = ["周一","周二","周三","周四","周五","周六","周日"]
        the_allmoney_list = [800,700,500,600,500,400,900]
        the_allpoints_list = [200,300,100,200,300,100,400]
        ######################################################
        line = (
            Line()
                .add_xaxis(xaxis_data=the_abscissa_list)
                .add_yaxis(series_name="营业总额", y_axis=the_allmoney_list, symbol="circle", is_symbol_show=True,is_smooth=True,is_selected=True)
                .add_yaxis(series_name="积分总额", y_axis=the_allpoints_list, symbol="circle", is_symbol_show=True,is_smooth=True,is_selected=True)
                .set_global_opts(title_opts=options.TitleOpts(title="每周营收折线图"))
        )

        #############################################
        the_sourceFile_origin = ("D:/monthcountview.html")
        line.render(path=the_sourceFile_origin)
        self.webview.load(QUrl.fromLocalFile(the_sourceFile_origin))



################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
