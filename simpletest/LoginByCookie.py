# coding: UTF-8

##
# 程序注释：
# 人人网的登陆地址需要用BeautifulSoup来抓取
# 个人信息存储在字典info中，info是一个包含账号密码的特殊的字典，具体的格式可能跟其他的网址不一样这一点应该注意一下。
# 比如人人网的格式为： {'form_email':'XXXX@XX.XX','form_password':'XXXXXXXXXXX'}
# 使用Cookie的好处在于，登陆之后就可以使用Cookie中保存的信息作为头信息的一部分，利用已经保存的头信息接着访问网站
#
##



import urllib,urllib2,cookielib
from BeautifulSoup import BeautifulSoup

url = 'http://www.renren.com/SysHome.do'
# 获取到登陆URL
resp1 = urllib2.urlopen(url)
source = resp1.read()
soup1 = BeautifulSoup(source)
login_url = soup1('form',{'method':'post'})[0]['action']

# 通过Cookie进行登陆
# 存储了登录信息的字典info
info = {
    'form_email':'1064319632@qq.com',
    'form_password':'827049'
}

# cookie
cookiejar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
urllib2.install_opener(opener)

# 添加异常处理模块
try:
    resp2 = urllib2.urlopen(login_url,urllib.urlencode(info))
except urllib2.URLError,e:
    if(hasattr(e,'reason')):
        print 'reason:{0}'.format(e.reason)
    if hasattr(e,'code'):
        print 'code:{0}'.format(e.reason)