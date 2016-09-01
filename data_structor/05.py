# coding:utf-8
import sys
reload(sys)

sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/26'
#    __Desc__ = 输入三个整数x,y,z，请把这三个数由小到大输出。

# ls = []
# for iten in range(0,3):
#     ls.append(int(raw_input('请输入一个数字：\n')))
# ls.sort()

ls = [1,3,6,2,4,8,7,9,0]
target = []
for item in ls:
    target.append(item)
    target.sort()
    print target

print '输入的数据由大到小的顺序为：\n',target