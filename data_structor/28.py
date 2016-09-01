# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/1'
#    __Desc__ = 查找字符串。　　

# 返回第一次出现该子字符串的位置，从零开始计数
def find(full_str,sub_str):
    return full_str.find(sub_str)


# 采用自定义的"哈希算法"，其实就是朴素的KMP算法实现。
# 本来是想把full_str改装成多个长度和sub_str的字符串相等长度的数组来计算其哈希和，相等的话作进一步的判断，但是Python实现起来略显复杂
def kmp(full_str,sub_str):
    sub_length = len(sub_str)
    full_length= len(full_str)

    for item in range(0,full_length-sub_length):
        # 设置 判断令牌
        flag = False
        # 对每一个子串进行验证
        for validate in range(0,sub_length):
            if full_str[item+validate]==sub_str[validate]:
                flag=True
            else:
                flag = False
            # 如果令牌为真，且长度刚好验证到sub_str的全部长度
            if flag and validate==sub_length-1:
                return item


if __name__=="__main__":
    full = "I am a handsome boy"
    sub = " a"
    print find(full,sub)
    print kmp(full,sub)
