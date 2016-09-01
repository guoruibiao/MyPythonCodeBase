# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/24'
#    __Desc__ = 

'''
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
'''

source = [1,2,3,4]

for i in range(len(source)):
    for j in range(len(source)):
        for k in range(len(source)):
            if source[i]!=source[j] and source[i]!=source[k] and source[j]!=source[k]:
                print source[i],source[j],source[k]