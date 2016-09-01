# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/1'
#    __Desc__ = 某个公司采用公用电话传递数据，数据是四位的整数，
# 在传递过程中是加密的，加密规则如下：每位数字都加上5,
# 然后用和除以10的余数代替该数字，再将第一位和第四位交换，
# 第二位和第三位交换。

def decode(number):
    ge = number%10
    shi = (number%100-ge)/10
    bai = (number%1000-10*shi-ge)/100
    qian = number/1000
    ge,shi,bai,qian= (ge+5)%10,(shi+5)%10,(bai+5)%10,(qian+5)%10
    qian,ge = ge,qian
    bai,shi = shi ,bai
    return qian*1000+bai*100+shi*10+ge

if __name__ == '__main__':
    number = 1221
    print decode(number)