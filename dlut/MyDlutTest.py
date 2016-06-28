# coding : UTF-8

import urllib,urllib2,re

def getHtml(url):
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

def writeToLocal(path,name,data):
    file = open(path+name,'wb')
    file.write(data)
    file.close()
    print 'Write Operation Success!'

#-------------------------------------------------------------Test Begin

headers = {
    'Referer':'http://zhjw.dlut.edu.cn/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}

filepath = "F:\\pachong\\dlut"
request_url = 'http://zhjw.dlut.edu.cn/loginAction.do'
data = getHtml(request_url)
writeToLocal(filepath,"dlut.html",data)
print "Enjoy the fly"