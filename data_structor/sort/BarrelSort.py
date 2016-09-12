# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/6'
#    __Desc__ = 桶排序算法，代码实现

def sort(arr):
    result = []
    for index in range(0,len(arr)):
        result.append(0)
    for index in range(len(arr)):
        counter = result[arr[index]]+1
        result[arr[index]]=counter
    return result

if __name__ == '__main__':
    arr = [1,3,5,7,9,2,9,4,6,8,0,1,1,3,2,2,2,2]
    arr = sort(arr)
    for item in range(len(arr)):
        if arr[item]!=0:
            step = arr[item]
            while step>0:
                print item,
                step-=1