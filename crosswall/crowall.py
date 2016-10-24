# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/10/24'
#    __Desc__ = 翻墙助手， 默认会先备份一下当前的hosts文件，防止出现意外，另外可以跨平台使用

import platform
import os


def crosswall(systemtype='Window'):
    try:
        if systemtype == 'Windows':
            os.system('copy %SystemRoot%\System32\drivers\etc\hosts  %SystemRoot%\System32\drivers\etc\hosts_bak')
            os.system('copy hosts.txt %SystemRoot%\System32\drivers\etc\hosts')
            os.system('ipconfig /flushdns')
            print 'It\'s done on Windows! And Try your browser!'
        elif systemtype == "Linux":
            os.system('cp /etc/hosts /etc/hosts_bak')
            os.system('mv ./hosts /etc/hosts')
            os.system('sudo /etc/init.d/networking restart ')
            print 'It\'s done on Linux! And Try your browser!'
    except Exception as e:
        print e



if __name__ == '__main__':
    crosswall(platform.system())