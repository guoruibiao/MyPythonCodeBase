# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/26'
#    __Desc__ = 输出9*9乘法口诀表。


for x in range(1,10):
    for y in range(1,x+1):
        # 原来实现Python2.7print的输出不换行的关键在于句末的一个小逗号啊！！！
        print "%d*%d=%d\t"%(x,y,x*y),
    print '\n'

