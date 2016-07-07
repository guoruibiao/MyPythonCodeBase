# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/7'
#    __Desc__ = 简单的tcpsocket的实现

from socket import *
from time import ctime

HOST = ''
PORT = 9999
BUFFERSIZE = 1024
ADDRESS = (HOST,PORT)

s = socket(AF_INET,SOCK_STREAM)
s.bind(ADDRESS)
s.listen(5)

while True:
    print 'Waiting for clients cennect!'
    tcpclient,addr = s.accept()
    print 'Connected By ',addr

    while True:
        try:
            data = tcpclient.recv(BUFFERSIZE)
        except Exception,e:
            print e.message
            tcpclient.close()
            break
        if not data:
            print "No Data received!"
            break
        senddata = 'Hi,you send me:[%s]%s'%(ctime(),data.encode('utf8'))
        tcpclient.send(senddata.encode('utf8'))
        print addr,' Says:',ctime(),data.encode('utf8')

tcpclient.close()
s.close()
