# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/26'
#    __Desc__ = 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

ls = [1,1]
for item in range(0,6):
    top = ls[-1]
    sec_top = ls[-2]
    ls.append((top+sec_top))
    ls.sort()

for item in range(len(ls)):
    print '第%d个月，兔子数量为：%d'%(item+1,ls[item])