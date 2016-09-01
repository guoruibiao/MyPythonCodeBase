# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/1'
#    __Desc__ = 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

#
def swap(arr):
    max_index = 0
    min_index = 0
    max = arr[0]
    min = arr[0]
    for item in range(len(arr)):
        if max<arr[item]:
            max = arr[item]
            max_index = item
        if min > arr[item]:
            min = arr[item]
            min_index = item
    max,arr[0] = arr[0],max
    min,arr[len(arr)-1] = arr[len(arr)-1],min
    return arr


if __name__ =="__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    print'交换前：',arr
    print '交换后：',swap(arr)
