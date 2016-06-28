# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/26'
#    __Desc__ = 试试看看能不能刷新自己的博客的浏览量

import urllib2,re
from bs4 import BeautifulSoup
from time import *

def getHtml(url,headers):
    req = urllib2.Request(url,headers=headers)
    page = urllib2.urlopen(req)
    html = page.read()
    return html

def parse(data):
    content = BeautifulSoup(data,'lxml')
    return content

def getReadNums(data,st):
    reg = re.compile(st)
    return re.findall(reg,data)

url = 'http://blog.csdn.net/Marksinoberg/article/details/51510052'
headers = {
    'referer':'http://blog.csdn.net/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}

i = 0
while True:
    html = getHtml(url,headers)
    content = parse(html)
    result = content.find_all('span',class_='link_view')
    print result[0].get_text()
    # i = i +1
    sleep(10)

