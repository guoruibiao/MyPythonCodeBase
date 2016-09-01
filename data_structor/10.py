# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/26'
#    __Desc__ = 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。


# 返回给定数字的水仙花计数值
def return_water_flower_number(number):
    ls = []
    i = 0
    while True:
        i = number %10
        ls.append(i)
        number = (number -i)/10
        if number ==0:
            break
    sum_sum = 0
    for item in ls:
        sum_sum+=int(item)**3
    return sum_sum



if __name__=="__main__":
    for i in range(1,10000):
        if return_water_flower_number(i)==i:
            print i