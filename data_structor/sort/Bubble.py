# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/2'
#    __Desc__ = 冒泡排序


def buddle_sort(ls):
    counter = 0
    for i in range(len(ls)):
        for j in range(0,len(ls)-i-1):
            if ls[j]>ls[j+1]:
                counter +=1
                ls[j],ls[j+1]=ls[j+1],ls[j]
                print ls
    print "共操作了：%d次！"%counter
    return ls


def better_buddle_sort(ls):
    counter = 0
    for i in range(len(ls)):
        flag = True
        for j in range(0,len(ls)-1-i):
            if ls[j]>ls[j+1]:
                counter +=1
                flag = False
                ls[j],ls[j+1]= ls[j+1],ls[j]
        if flag :return ls
    print "共操作了：%d次！" % counter
    return ls


if __name__ == '__main__':
    ls = [2,3,5,1,4,0,8,6,7,9,1,0]
    print buddle_sort(ls)
    ls2 = [2,3,5,1,4,0,8,6,7,9,1,0]
    print better_buddle_sort(ls2)