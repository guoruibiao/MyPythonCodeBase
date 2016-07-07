# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/7'
#    __Desc__ = 创建一个简单的套接字监听请求

import socket

HOST = '192.168.59.255'
PORT = 9998

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',PORT))
print '套接字已启动！'
while True:
    data,addr = s.recvfrom(1024)
    print addr,str(' : ')+data

