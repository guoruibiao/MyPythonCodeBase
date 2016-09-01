# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/1'
#    __Desc__ = 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

# 将后面的M个数字全部转到前面，且顺序保持不变。利用了列表的分片操作
def shift_right(ls,number):
    temp = ls[len(ls)-number:]
    ls = ls[0:len(ls)-number]
    for item in range(0,len(ls)):
        temp.append(ls[item])
    return temp

if __name__ == '__main__':
    ls = [1,2,3,4,5,6,7]
    print shift_right(ls,3)
