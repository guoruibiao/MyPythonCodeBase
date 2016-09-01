# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/26'
#    __Desc__ = 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

def retravel(number,times):
    result = 0
    tag = number
    for index in range(1,times+1):
        result += number
        number = number*10+tag

    return result

if __name__=="__main__":
    number = int(raw_input('请输入0-9之间的一个数字：\n'))
    times = int(raw_input('请输入要循环的次数：\n'))
    print '结果是：',retravel(number,times)