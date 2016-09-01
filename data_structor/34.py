# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/1'
#    __Desc__ = 列表转换为字典。

# 系统内置的实现，也即是一个列表对应一个字典项，所以长度当且仅当为2！！！
def build_in(ls_key,ls_value):

    # 列表项中的元素数据至多为2两个
    # print dict([ls_value, ls_key])
    return dict([ls_key,ls_value])

# 自定义的实现，key集合匹配value集合实现列表转字典
def my_translator(ls_key,ls_value):
    if len(ls_key)!=len(ls_value):
        print "键值对的长度不匹配！"
        exit(0)
    dict = {}
    for item in range(len(ls_key)):
        dict[ls_key[item]]=ls_value[item]
    return dict

if __name__ == '__main__':
    ls_key = ['x', 'y']
    ls_value = [1, 2]
    print build_in(ls_key,ls_value)
    ls_key.append('z')
    ls_value.append(3)
    print my_translator(ls_key,ls_value)
