# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/7'
#    __Desc__ = 简单的tcp socket客户端的实现

from socket import *

class TcpClient:
    # HOST = 'localhost'
    PORT = 9999
    HOST = '192.168.59.225'
    BUFFSIZ = 1024
    ADDR = (HOST,PORT)
    def __init__(self):
        self.client = socket(AF_INET,SOCK_STREAM)
        self.client.connect((self.HOST,self.PORT))

        while True:
            senddata = raw_input('>>>')
            if not senddata:
                print 'Please input some words!\n>>>'
                continue
            if senddata == "quit":
                break
            self.client.send(senddata.encode('utf8'))
            recvdata = self.client.recv(self.BUFFSIZ)
            if not recvdata:
                break
            print recvdata.encode('utf8')

if __name__ == "__main__":
    client = TcpClient()