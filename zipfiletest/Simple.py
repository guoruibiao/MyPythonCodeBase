# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/6'
#    __Desc__ = zipfile test

import zipfile

zFile = zipfile.ZipFile("file.zip")
file = open(r'./directory.txt','rb')
for line in file.readlines():
    try:
        passwd = line.strip('\n')
        zFile.extractall(pwd=passwd)
        print "密码为："+str(passwd)
    except Exception,e:
        pass
file.close()
