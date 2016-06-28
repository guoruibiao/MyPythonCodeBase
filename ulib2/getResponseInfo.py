# coding:UTF-8

# 这个程序的作用就是输出网站返回的数据的详细信息
# 其中主要是用到了： ls.items()来将其转换成键值对形式
import sys,urllib2

def getInfo(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    info = response.info()
    return info

def printInfo(ls):
    print "数据开始-------------------"
    for key,value in ls.items():
        print "%s  = %s " %(key,value)
    print "数据输出结束----------------"

url = 'http://www.baidu.com'
info = getInfo(url)
printInfo(info)