# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/26'
#    __Desc__ = 一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。

def is_full_number(number):
    ls = []
    i = 1
    for i in range(1,number):
        if number %i==0:
            ls.append(i)
            if i+1== number:
                break
        else:
            continue
    summary = 0
    for i in ls:
        summary +=i
    if summary == number :
        return True
    else:
        return False

if __name__ == "__main__":
    for i in range(1,10000):
        if is_full_number(i):
            print i
