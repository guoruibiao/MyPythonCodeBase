# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/1'
#    __Desc__ = 使用lambda来创建匿名函数。关键在于lambda表达式紧跟参数，以分号分隔后的表达式只能为算术逻辑表达式，不能有判断等语句

MAX = lambda x,y: (x>y)*x + (x<y)*y
MIN = lambda x,y: (x<y)*x + (x>y)*y
SUM = lambda x,y: x+y
SUB = lambda x,y: (x>y)*(x) + (x<y)*(y-x)
MUT = lambda x,y:(x!=0)*(x*y) or 0
DIV = lambda x,y: (x*y!=0)*(((float)(x)/(float)(y))) or "除数不能为0！"

if __name__=="__main__":
    x = 10
    y = 100
    print "MAX:",MAX(x,y)
    print "MIN:",MIN(x,y)
    print "SUM:",SUM(x,y)
    print "SUB:",SUB(x,y)
    print "SUB:" , SUB(y, x)
    print "MUT:",MUT(x,y)
    print "DIV:",DIV(x,y)
    print "DIV:" , DIV(y, x)