# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/26'
#    __Desc__ = 判断101-200之间有多少个素数，并输出所有素数。

def is_sushu(number):
    for item in range(2,number):
        if number%item==0:
            return False
    return True

if __name__=="__main__":
    for i in range(101,201):
        if is_sushu(i):
            print i

