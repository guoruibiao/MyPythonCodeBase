# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/1'
#    __Desc__ = 交换两个数的值
# 其实原理都是一样的，只不过Python可以借助于tuple，元组的形式来一次性的返回多个值
# 相对于其他编程语言而言，这真的很方便


def change(a,b):
    temp = a
    a = b
    b = temp
    return a,b

def exchange(a,b):
    a,b = b,a
    return a,b

if __name__=="__main__":
    a ,b = 1,2
    print '原来的值：%d---%d'%(a,b)
    a,b = exchange(a,b)
    print '值交换后：%d---%d' % (a, b)
    c,d = change(a,b)
    print '值交换后：%d---%d' % (a, b)
    print type(change(a,b))
