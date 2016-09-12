# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/6'
#    __Desc__ = 归并排序

def merge(arr,start,mid,end):
    len1 = mid-start+1
    len2 = end-mid
    i=j=k=0
    left_list = right_list = []
    for i in range(0,len1):
        left_list[i] = arr[i+start]
    for i in range(0,len2):
        right_list[i] = arr[i+mid+1]

    i = j = 0
    k = start
    while k<end:
        if i==len1 or j == len2:
            break
        if left_list[i]<=right_list[j]:
            arr[k] = left_list[i]
            i+=1
        else:
            arr[k] = right_list[j]
            j+=1

    while i<len1:
        arr[k] = right_list[i]
        k+=1
        i+=1

    while j<len2:
        arr[k] = left_list[j]
        k+=1
        j+=1


def mergeSort(arr,start,end):
    if start< end:
        mid = (start+end)/2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid,end)
    return arr

if __name__ == '__main__':
    arr = [1,3,5,7,9,2,4,6,8,0]
    arr = mergeSort(arr,0,len(arr)-1)
    print arr
