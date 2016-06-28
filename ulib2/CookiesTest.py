# coding: UTF-8

import urllib2,cookielib
cookie = cookielib.CookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_support)
urllib2.install_opener(opener)

content = urllib2.urlopen('http://www.baidu.com').read()

print len(content)

# 从这里我们就可以看到 在访问完一个网址后，Cookie是被记录下来的，虽然只是在内存中！
for key in cookie:
    print str(key) + '  ：  ' + str(key.value)