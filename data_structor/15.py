# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/26'
#    __Desc__ = 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

def get_total_peaches(day):
    total_peaches = 0
    if day == 10:
        total_peaches = 1
    else:
        total_peaches = (get_total_peaches(day+1)+1)*2
    return total_peaches

print 'total peaches is:%d'%get_total_peaches(1)