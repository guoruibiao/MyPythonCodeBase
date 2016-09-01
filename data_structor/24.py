# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/1'
#    __Desc__ = 输出一个随机数。

from random import *


# 返回的是整数
def rand_arrange_in(a, b):
    return randint(a, b)


# 返回的不是整数
def rand_uniform(a, b):
    return uniform(a, b)


if __name__ == "__main__":
    start = 10
    end = 28
    print "---------------单个数字-------------------------"
    print "random int:%d" % rand_arrange_in(start, end)
    print "random uniform:%d" % rand_uniform(start, end)
    print "---------------多个数字-------------------------"
    print "random int:\n"
    for item in range(0, 10):
        print rand_arrange_in(start, end),
    print "\nrandom uniform:"
    for item in range(0, 10):
        print rand_uniform(start, end),
