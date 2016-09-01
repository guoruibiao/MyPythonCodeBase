# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/26'
#    __Desc__ = 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

def get_total_height(height,times):
    total_height = float(height)
    temp_height = 0.0
    for i in range(1,times):
        height = float(height) /2
        temp_height = height
        total_height+=2*height
    return (total_height,temp_height)

if __name__=="__main__":
    height = 100.0
    times = 10
    print "所求高度和为：%d,最后一次落地弹起高度为：%d"%get_total_height(height,times)
