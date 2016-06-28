# coding:UTF-8
import re,urllib,urllib2

def getHtml(url, data = None,headers = None):
    if data : data = urllib.urlencode(data)
    request = urllib2.Request(url,data,headers)
    page = urllib2.urlopen(request)
    return page.read()

def getComments(page,reg):
    myreg = re.compile(reg)
    comments = re.findall(myreg, page)
    return comments

if __name__ == "__main__":
    url = 'http://www.jianshu.com/p/4d9d03287670'
    headers = {
        'Referer':'http://www.jianshu.com/p/4d9d03287670',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
    }
    page = getHtml(url,headers=headers)
    reg = r'<div class="(.+)"'
    comments = getComments(page,reg)
    for item in comments:
        print item