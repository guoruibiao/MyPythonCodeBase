# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/6'
#    __Desc__ = 希尔排序,核心算法思想：以给定的步长来分隔每一次排序的范围，不断缩小以达到整体排序的目的

#  每次排序输出的情况
# D:\Software\Python2\python.exe E:/Code/Python/DataStructor/temp/ShellSort.py
# [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# [1, 3, 5, 7, 0, 2, 4, 6, 8, 9]
# [1, 3, 5, 7, 0, 2, 4, 6, 8, 9]
# [0, 3, 1, 7, 5, 2, 4, 6, 8, 9]
# [0, 3, 1, 7, 4, 2, 5, 6, 8, 9]
# [0, 3, 1, 7, 4, 2, 5, 6, 8, 9]
# [0, 3, 1, 7, 4, 2, 5, 6, 8, 9]
# [0, 2, 1, 3, 4, 7, 5, 6, 8, 9]
# [0, 2, 1, 3, 4, 6, 5, 7, 8, 9]
# [0, 2, 1, 3, 4, 6, 5, 7, 8, 9]
# [0, 2, 1, 3, 4, 6, 5, 7, 8, 9]
# [0, 1, 2, 3, 4, 6, 5, 7, 8, 9]
# [0, 1, 2, 3, 4, 6, 5, 7, 8, 9]
# [0, 1, 2, 3, 4, 6, 5, 7, 8, 9]
# [0, 1, 2, 3, 4, 6, 5, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Process finished with exit code 0


def shell(arr):
    step = len(arr)/2
    while step>=1:
        for k in range(0,step):
            i = k+step
            while i<len(arr):
                temp = arr[i]
                j = i-step
                i+=step
                while j>=k and arr[j]>temp:
                    arr[j+step] = arr[j]
                    j-=step
                arr[j+step] = temp
                print arr
        step /=2
    return arr

if __name__ == '__main__':
    arr = [1,3,5,7,9,2,4,6,8,0]
    arr = shell(arr)
    print arr
