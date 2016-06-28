# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/26'
#    __Desc__ = 通过在本地读取一个文件内容来实现电脑关机操作

import os,sys
import re
from time import *

def getCmd(fullfilename):
    file = open(fullfilename, 'r')
    data = file.readlines()
    cmds = []
    for item in data:
        cmds.append(item.split(':')[1])
    return cmds



# while 1:
print asctime()
file = 'example.txt'
command = getCmd(file)
result = str(os.system(command[1]))
wf = open('dir.txt','wb')
wf.write(result)
wf.close()
print '命令已经写入到了文件！'

