# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/31'
#    __Desc__ = 文本颜色设置


# 类似于shell形式的编写，可以改变终端下字体的颜色，达到一个很好的变成体验的效果
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.OKGREEN + "警告的颜色字体?"+bcolors.UNDERLINE+"第二个颜色显示"
