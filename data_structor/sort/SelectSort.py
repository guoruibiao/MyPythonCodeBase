# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/6'
#    __Desc__ = 选择排序，核心算法思想即：每次选择出最小的数并实现排序效果

# 每次选择排序后的输出结果
# D:\Software\Python2\python.exe E:/Code/Python/DataStructor/temp/SelectSort.py
# [0, 3, 5, 7, 9, 2, 4, 6, 8, 1]
# [0, 1, 5, 7, 9, 2, 4, 6, 8, 3]
# [0, 1, 2, 7, 9, 5, 4, 6, 8, 3]
# [0, 1, 2, 3, 9, 5, 4, 6, 8, 7]
# [0, 1, 2, 3, 4, 5, 9, 6, 8, 7]
# [0, 1, 2, 3, 4, 5, 9, 6, 8, 7]
# [0, 1, 2, 3, 4, 5, 6, 9, 8, 7]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Process finished with exit code 0
def select(arr):
    for i in range(len(arr)):
        max_index = i

        j = i
        while j< len(arr):
            if arr[max_index]> arr[j]:
                max_index = j
            j +=1
        if max_index!=i:
            arr[max_index],arr[i]= arr[i],arr[max_index]
        print arr
    return arr

if __name__ == '__main__':
    arr = [1,3,5,7,9,2,4,6,8,0]
    arr = select(arr)
    print arr