### 文章说明
编程过程中，出现BUG不可避免，所以经常要进行调试.
在[廖雪峰的python3教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)中，有一篇专门讲[调试的文章](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431915578556ad30ab3933ae4e82a03ee2e9a4f70871000)，简单列举了调试的几种方法，建议先进行阅读，了解一下。

为更方便新手学习，我结合自身开发情况，进一步补充一下。

### 一.print大法
如果不是确定要记录到日志，一般用的最多的还是print。
print()内置函数，一般最初学习python的时候，就接触到了，这里再列举一下几种调试常用的print用法。

>1.直接打印数字
print(111111111)                        

>2.直接打印文字
print("进来了")                   

>3.直接打印变量  
print(name)                       

>4.打印文字+变量  
print("进来了"+name)                           

>5.打印文字+变量 
print("进来了" , name)                       

>6.打印文字+变量
print("进来了，名字是%s，年龄是%d" % (name , age))                       

### 二.IDE断点调试
如图所示，为PyCharm的调试。
（注：图为网页分享，并非原创。找不到原图链接了，抱歉。）

![](https://upload-images.jianshu.io/upload_images/1724251-b2d707c7152b1c6c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 三.终极武器logging
python有一个标准库logging，用来管理日志。
通过整个标准库，可以进一步构建自己的日志模块。
如下是一个自定义的日志模板。
（注：整个模块是网友分享，并非原创。找不到原文链接了，抱歉。）

```python
import time
import logging
from logging.handlers import TimedRotatingFileHandler
####################################
#日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。

print_level = logging.DEBUG    #打印级别控制
file_path = "D:/TestDemo/"        #定义日志存放路径
file_name = time.strftime('%Y%m%d', time.localtime(time.time()))  #文件名称

####################################
class Log():
    # 构造函数
    def __init__(self, name):
        self.filename = file_path + file_name + '.log'  # 日志文件名称
        self.name = name  # 为%(name)s赋值

        #创建日志器
        self.logger = logging.getLogger(self.name)

        # 控制记录级别
        self.logger.setLevel(print_level)

        # 控制台日志
        self.console_handler   = logging.StreamHandler()
        console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s[line:%(lineno)d] - %(message)s')
        self.console_handler.setFormatter(console_format)

        # 文件日志
        self.filetime_handler  = TimedRotatingFileHandler(self.filename, 'D', 1, 30) #保留30天,1月保存一个文件
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s[line:%(lineno)d] - %(message)s')
        self.filetime_handler.setFormatter(file_format)

        # 为logger添加的日志处理器
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.filetime_handler)

    #测试
    def debug(self, msg):
        self.logger.debug(msg)

    #信息
    def info(self, msg):
        self.logger.info(msg)

    #警告
    def warning(self, msg):
        self.logger.warning(msg)

    #错误
    def error(self, msg):
        self.logger.error(msg)

    #重大错误
    def critical(self, msg):
        self.logger.critical(msg)

    #抛出异常
    def exception(self, msg):
        self.logger.exception(msg)

    #关闭控制台日志
    def close_console(self):
        self.logger.removeHandler(self.console_handler)

    # 关闭文件日志
    def close_filetime(self):
        self.logger.removeHandler(self.filetime_handler)

```
本文如有帮助，敬请留言鼓励。
本文如有错误，敬请留言改进。