# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/31'
#    __Desc__ = 按相反的顺序输出列表的值。

def reverse_print(list):
    end = len(list)-1
    while end>=0:
        print list[end]
        end-=1

# 使用系统的内建方法，分片技术
def reverse_slice(list):
    for item in list[::-1]:
        print item

def reverse(list=[]):
    reverse_list = []
    end = len(list)-1
    while end>=0:
        reverse_list.append(list[end])
        end-=1
    return reverse_list


if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9]
    # reverse_print(list)
    # result = reverse(list)
    # for item in result:
    #     print item,
    reverse_slice(list)