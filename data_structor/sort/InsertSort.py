# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/5'
#    __Desc__ = 插入排序 Python实现
#   实现的算法原理：
#   直接插入到数组的最后面，然后比较该数与前一个数的大小，如果小于前者，则交换位置，此时更新前者的下标以实现更新的判断
#   代码运行结果如下：
# D:\Software\Python2\python.exe E:/Code/Python/DataStructor/temp/InsertSort.py
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

def directInsert(arr):
    for p in range(len(arr)):
        temp = arr[p]
        i = p-1
        while i>=0 and arr[i]>temp:
            arr[i+1],arr[i]=arr[i],arr[i+1]
            i-=1
        print arr
        arr[i+1] = temp
    return arr

if __name__ == '__main__':
    arr = [1,3,5,7,9,2,4,6,8,0]
    arr = directInsert(arr)
    print arr

