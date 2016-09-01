# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/31'
#    __Desc__ = 按逗号分隔列表。

def devide_list(list):
    # 这里的str(item)必须添加，否则会导致字符串拼接的类型不匹配的异常
    return ','.join(str(item) for item in list)

if __name__ =="__main__":
    list = [1,2,3,4,5,6,7]
    print devide_list(list)
