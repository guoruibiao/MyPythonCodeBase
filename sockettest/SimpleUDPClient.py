# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/7'
#    __Desc__ = socket的客户端的简单实现

import socket

PORT = 9998
HOST = '192.168.59.255'
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
words = raw_input('Client:')
while words != 'quit':
    s.sendto(words,(HOST,PORT))
    words = raw_input('Client:')
s.close()