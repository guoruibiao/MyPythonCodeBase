# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/10/10'
#    __Desc__ = 

import re

def getemails(chatfile):
    file = open(chatfile, 'rb')
    data = file.read()
    file.close()

    reg = r'(\d{9,10})'
    ls = list(set(re.findall(reg, data)))

    emails = []
    for item in ls:
        emails.append(str(item) + str("@qq.com"))
    return emails

if __name__ == '__main__':
    chatpath = r'./qqqun.txt'

    emails = getemails(chatpath)
    print emails