# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/5'
#    __Desc__ = 快速排序

def partition1(arr,left,right):
    pivot = arr[left]
    while left < right:
        while left<right and arr[right]>=pivot:
            right -=1
        if left<right:
            arr[left] = arr[right]
            left +=1

        while left<right and arr[left]<=pivot:
            left +=1
        if left < right:
            arr[right] = arr[left]
            right -=1
    arr[left] = pivot
    return left

def quicksort1(arr,left,right):
    dp = 0
    if left < right:
        dp = partition1(arr,left,right)
        quicksort1(arr,left,dp-1)
        quicksort1(arr,dp+1,right)
    return arr

if __name__ == '__main__':
    arr = [1,3,5,7,9,2,4,6,8,0]
    quicksort1(arr,0,len(arr)-1)
    print arr
