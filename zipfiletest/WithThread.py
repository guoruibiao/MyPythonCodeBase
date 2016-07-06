# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/6'
#    __Desc__ = 使用多线程的方式进行暴力破解密码

import zipfile
from threading import Thread
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print 'the password is :'+str(password)
    except Exception , e:
        pass

def main():
    zFile = zipfile.ZipFile("./file.zip")
    passfile = open(r'./directory.txt','rb')
    for line in passfile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile,args=(zFile,password))
        t.start()


if __name__=="__main__":
    main()
