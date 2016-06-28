# coding:UTF-8

import urllib,urllib2,cookielib

filename = r'F:\pachong\gaoqing\dlutcookie.txt'
# show cookie and save to local
cookie = cookielib.MozillaCookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
postdata = urllib.urlencode({
    'zjh':'201492115',
    'mm':'285514'
})


# 登陆到教务系统的url
url = 'http://zhjw.dlut.edu.cn/loginAction.do'

# 开始进行模拟登陆，并把cookie保存到变量
response = opener.open(url,postdata)
cookie.save(filename,ignore_discard=True,ignore_expires=True)

# 打印一下获得的cookie信息吧
for item in cookie:
    item.name + ' = ' + item.value




# 利用cookie访问另一个网址   登陆到个人成绩的URL
course_url='http://zhjw.dlut.edu.cn/xkAction.do?actionType=6'
course_header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'referer':'http://zhjw.dlut.edu.cn/menu/s_main.jsp'
}

result = opener.open(course_url)
print result.read()
