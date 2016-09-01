# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/31'
#    __Desc__ = 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def isHuiWen(number):
    arr =  str(number)
    start = 0
    end = len(arr)-1
    flag = (end-start)/2
    while start <=end :
        print arr[start],arr[end]
        if arr[start]==arr[end]:
            start +=1
            end-=1
        else:
            return False
    return True



if __name__=="__main__":
    result = isHuiWen(123321)
    if result:
        print "Yes"
    else:
        print "NO!"
