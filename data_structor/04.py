# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/24'
#    __Desc__ = 输入某年某月某日，判断这一天是这一年的第几天？

year = int(raw_input('请输入年份:\n'))
month = int(raw_input('请输入月份:\n'))
day = int(raw_input('请输入日期：\n'))

days = [0,31,59,90,120,151,181,212,243,273,304,334]
result = 0
if 0< month <= 12:
    result = days[month]
else:
    result = 0

result += day

if year%400==0 or (year%4==0 and year%100!=0):

    if month >2 : result +=1

print '%d-%d-%d是今年的第%d天！'%(year,month,day,result)