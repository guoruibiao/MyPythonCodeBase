# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/24'
#    __Desc__ = 一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
import math

for i in range(1,10000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if (x*x == i + 100) and (y*y == i+268):
        print i
