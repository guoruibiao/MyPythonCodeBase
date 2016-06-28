# coding:UTF-8

# 使用代理的目的是为了防止IP在爬的过程中被封掉.这个案例有错误，我也不太清楚我的这个代理出现了什么错误
import urllib2
try:
    proxy = urllib2.ProxyHandler({'http':'192.168.57.209:6666'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.baidu.com')
    print len(response.read())
except Exception :
    print str(Exception)