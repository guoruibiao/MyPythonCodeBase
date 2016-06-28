# coding:UTF-8

import urllib,urllib2
from bs4 import BeautifulSoup
# http://blog.csdn.net/marksinoberg/article/details/51418017  http://blog.csdn.net/marksinoberg/article/details/51424150
url = 'http://blog.csdn.net/marksinoberg/article/details/51418017'
headers = {
    'referer':'http://blog.csdn.net/marksinoberg/article/details/51418017',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}

request = urllib2.Request(url,headers= headers)
page = urllib2.urlopen(request).read()
soup = BeautifulSoup(page,'html.parser',from_encoding='GB18030')
# 获得文章的标题
titleJar = soup.select('[class="article_title"]')
title = titleJar[0].select('a')
print "文章发布时候的标题是:   "
print title[0].text
# 获得文章的主体。由于每一个小标题都会被认为是一个H标签，所以要进行循环的读取
bodyJar = soup.select('[class="markdown_views"]')
# 获得一个文章中的所有小标题组成的列表
article_titles = bodyJar[0].select('h2')
# 获得每一个标题下面的文章的片段的内容
print "下面是文章的正文部分："
for item in range(len(article_titles)):
    print article_titles[item].text
    print bodyJar[0].select('p')[item].text