### 相关说明
本文给出的是TCP协议的Socket编程。

其中用了一个dbmanager数据库操作模块，这个模块是我自己定义的，可以在我的另一个文章中找到这个模块的分享。[python操作mysql数据库的精美实用模块](https://www.jianshu.com/p/3785e36fad95)
### 服务段完整代码
【如下代码，完全复制，直接运行，即可使用】

```python
import socket
import threading
import json
from tools import dbmanager    #这个模块是我自定义的，可以在我的另一个文章中找到这个模块的分享
###################################
####服务器参数
####################################

HOST = '0.0.0.0'            #ip 0.0.0.0 表示本机所有ip地址
PORT = 9905                 #端口号
Max_Listen =10              #最大监听数
BUFSIZ = 1024               #每次接收数据长度
ENDMARK = "messageover"     #信息结束标记



####################################
####业务处理函数
####################################
def searchuser(sock, dict_data):
    the_searchstring = dict_data['par']
    #########构造sql语句
    sqlstring0 = "SELECT * FROM hr_user WHERE id>0 "

    if the_searchstring != None and the_searchstring != "":
        sqlstring0 = sqlstring0 + " AND (username LIKE '%" + the_searchstring + "%')"

    ########执行数据库查询
    data0 = dbmanager.executeSelectAllback(sqlstring0)
    if data0 == False:
        message = {'action': 'Error_SqlConnet'}
        sock.sendall(json.dumps(message).encode("utf-8"))    ####发送数据给客户端
        return
    if data0 != None:
        message = {'action': 'SearchUser_Success'}
        message['data'] = data0
        sock.sendall(json.dumps(message).encode("utf-8"))    ####发送数据给客户端
        return



####################################
####线程处理函数
####################################
def readRequest(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    allresponse = ""
    while True:
        ########接收数据
        data = sock.recv(BUFSIZ).decode('utf-8')
        if len(data):
            allresponse = allresponse + data
            if ENDMARK not in allresponse:
                continue
        if allresponse == "":
            break


        ########处理数据
        allresponse =allresponse[:-len(ENDMARK)]
        dict_data = json.loads(allresponse)
        action = dict_data['action']
        if action == "SearchUser":
            searchuser(sock, dict_data)  #业务处理
            break
        elif action == "SearchCompany":
            break                        #业务处理
        else:
            break


    ########关闭连接
    sock.close()
    print('Connection from %s:%s closed.' % addr)








####################################
#程序入口
####################################
if __name__ == "__main__":
    #####创建一个socket
    the_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET指定使用IPv4协议  #SOCK_STREAM指定使用面向流的TCP协议

    #####绑定端口
    the_socket.bind((HOST, PORT))

    #####监听端口
    the_socket.listen(Max_Listen)

    print('Waiting for connection...')

    while True:
        # 接受一个新连接
        sock, addr = the_socket.accept()

        # 创建新线程来处理TCP连接
        the_thread = threading.Thread(target=readRequest, args=(sock, addr))
        the_thread.start()
    ####################################
```


### 客户端完整代码
【如下代码，完全复制，直接运行，即可使用】
```python
import socket
import json

#############################################################################################
####参数
#############################################################################################
HOST = '127.0.0.1'
PORT = 9905
BUFSIZ = 1024
ENDMARK = "messageover"



#############################################################################################
#######请求处理函数
#############################################################################################
def issueRequest(action, par):
    # 创建一个socket
    the_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 建立连接:
    try:
        the_socket.connect((HOST, PORT))
    except:
        print("服务器连接失败！")
        return

    #############################
    try:
        ########发送数据:
        message = {}
        message['action'] = action
        message['par'] = par
        last_message = json.dumps(message) + ENDMARK  # son.dumps()将 Python 对象编码成 JSON 字符串
        print(message)
        the_socket.sendall(last_message.encode("utf-8"))

        ########接收数据
        allresponse = ""
        while True:
            response = the_socket.recv(BUFSIZ).decode('utf-8')
            if len(response):
                allresponse = allresponse + response
                continue
            if allresponse == "":
                break

            #######处理数据
            dict_data = json.loads(allresponse)  # json.loads()将已编码的 JSON 字符串解码为 Python 对象
            action = dict_data['action']
            if action == "SearchUser_Success":
                data0 = dict_data['data']
                print(data0)
                break
            elif action == "Error_SqlConnet":
                print("数据查询失败！")
                break
            else:
                break
    except:
        print("服务器连接异常，数据查询失败！")
    finally:
        #######关闭连接
        the_socket.close()



####################################
#程序入口
####################################
if __name__ == "__main__":
    the_searchstring ="张三"
    issueRequest("SearchUser", the_searchstring)
```
本文如有帮助，敬请留言鼓励。
本文如有错误，敬请留言改进。