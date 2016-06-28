# coding:UTF-8

# 这个程序是用来测试使用GET方式以及POST方式向服务器提交信息

import sys,urllib,urllib2

# GET
def ByGet(url,params):
    url = url + '?' + urllib.urlencode(url,[('query',params)])
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    page = response.read()
    print "数据已经通过GET方式成功提交"

def ByPost(url,params):
    data = urllib.urlencode(url,[('query',params)])
    request = urllib2.Request(url)
    response = urllib2.urlopen(request,data)
    page = response.read()
    print "数据已经通过POST的方式成功的提交了出去！"

def CommonWay():
    url = 'http://localhost:8080/Test/GetParameters'
    params = {
        'username':'Username',
        'password':'Password'
    }
    data = urllib.urlencode(params)
    req = urllib2.Request(url,data)
    response = urllib2.urlopen(req)
    content = response.read()
    print content

CommonWay()
print "Succeed!"

# url = 'http:// 192.168.58.25:8080/Test/index.html'
# lpage = urllib.urlopen("http://localhost:8080/Test/index.html?username='GUORUIBIAO'&password='Password'")
# html = page.read()
# htm