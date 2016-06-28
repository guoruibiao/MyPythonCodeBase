# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/26'
#    __Desc__ = 以网页的方式控制电脑

from urllib2 import *
from bs4 import BeautifulSoup

def getHtml(url):
    page = urlopen(url).read()
    return page

def getTitle(data):
    data=BeautifulSoup(data,'lxml')
    return data.title

url = 'http://www.baidu.com'
response = getTitle(getHtml(url)).text
if response == u"百度一下，你就知道":
    os.system('shutdown -s -t 120 -c "This is controlled by web page. My Name is Mark!"')
print 'Bye-Bye'





