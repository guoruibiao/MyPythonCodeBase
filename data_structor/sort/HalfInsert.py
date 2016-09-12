# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/5'
#    __Desc__ = 折半插入实现排序。算法核心在于不断的折半，来缩小排序的范围。核心在于对有序列表的插入排序

# 每次交换后的排序输出结果
# D:\Software\Python2\python.exe E:/Code/Python/DataStructor/temp/HalfInsert.py
# [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# [1, 2, 3, 5, 7, 9, 4, 6, 8, 0]
# [1, 2, 3, 4, 5, 7, 9, 6, 8, 0]
# [1, 2, 3, 4, 5, 6, 7, 9, 8, 0]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Process finished with exit code 0
#

def halfInsert(arr):
    right = left = mid = p = 0
    for p in range(len(arr)):
        temp = arr[p]
        left = 0
        right = len(arr)-1
        while left <=right:
            mid = (left+right)/2
            if temp > arr[mid]:
                left = mid+1
            else:
                right = mid-1

        i = p - 1
        while i>= left:
            arr[i+1]=arr[i]
            i-=1
        arr[left] = temp
        # 输出每一次折半插入后的排序结果
        print arr
    return arr

if __name__ == '__main__':
    arr = [1,3,5,7,9,2,4,6,8,0]
    arr = halfInsert(arr)
    print arr

