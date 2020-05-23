# Filename: PortListner.py
# @author: RobinTang
# Created on 2012-9-5 1:42:05

import sys
import threading
from socket import *

encoding = 'utf-8'
BUFSIZE = 1024


ip = sys.argv[1]

def myprobe(host,port,payload):
    global BUFSIZE
    ADDR = (host,port)
    tcpCliSock = socket(AF_INET,SOCK_STREAM)#创建客户端套接字
    tcpCliSock.connect(ADDR)#尝试连接服务器
    tcpCliSock.send(payload)#会话（发送/接收）
    data=tcpCliSock.recv(BUFSIZE)
    tcpCliSock.close()#关闭客户端套接字

    return data



# a read thread, read data from remote
class Sender(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        
    def run(self):
        while True:
            data = self.client.recv(BUFSIZE)
            if(data):
                string = bytes.decode(data, encoding)
                print(string)
                myprobe(ip, 666, string)
            else:
                break
        print("close:", self.client.getpeername())
        
    def readline(self):
        rec = self.inputs.readline()
        if rec:
            string = bytes.decode(rec, encoding)
            if len(string)>2:
                string = string[0:-2]
            else:
                string = ' '
        else:
            string = False
        return string
 
# a listen thread, listen remote connect
# when a remote machine request to connect, it will create a read thread to handle
class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", port))
        self.sock.listen(0)
    def run(self):
        print("listener started")
        while True:
            client, cltadd = self.sock.accept()
            Sender(client).start()
            cltadd = cltadd
            print("accept a connect")
 
lst  = Listener(9011)   # create a listen thread
lst.start() # then start
 
# Now, you can use telnet to test it, the command is "telnet 127.0.0.1 9011"
# You also can use web broswer to test, input the address of "http://127.0.0.1:9011" and press Enter button
# Enjoy it....