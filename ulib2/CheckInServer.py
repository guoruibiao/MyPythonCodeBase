# coding: UTF-8

# 这个程序大致是经过服务器端验证，允许在需要的时候访问用户名和密码
# 然后调用build_opener（）指定一些额外处理。原理urllib2.urlopen()等同于opener.open()

import sys,urllib2,getpass

# 一个针对于urllib2.HTTPPasswordMgr的包装类，允许在需要的时候询问用户名和密码，然后调用builder_opener()制定一些额外的处理
class BasePassword(urllib2.HTTPPasswordMgr):
    def find_user_password(self,realm,authurl):
        ret = urllib2.HTTPPasswordMgr.find_user_password(self,realm,authurl)

        if(ret[0] == None and ret[1] == None):
            sys.stdout.write('Login required for %s and %s' %(realm,authurl))
            sys.stdout.write("Username: ")
            username = sys.stdin.readline().rstrip()
            password = getpass.getpass().rstrip()
            return (username,password)
        else:
            return ret
# 添加了Cookie的url可以被成功的访问
#url = 'http://q14.cnzz.com/stat.htm?id=1255621432&r=http%3A%2F%2Fid.amap.com%2Findex%2Fcross%3Fref%3Dhttp%3A%2F%2Flbs.amap.com%2Fdev%2Fregister%2Fsuccess&lg=zh-cn&ntime=none&cnzz_eid=1292739110-1463048150-http%3A%2F%2Fid.amap.com%2F&showp=1366x768&t=%E6%88%90%E4%B8%BA%E5%BC%80%E5%8F%91%E8%80%85%20%7C%20%E9%AB%98%E5%BE%B7%E5%9C%B0%E5%9B%BE%E5%BC%80%E6%94%BE%E5%B9%B3%E5%8F%B0&h=1&rnd=1806388921'

# 未添加Cookie的访问
url = 'http://www.csdn.net/'
request = urllib2.Request(url)
opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler)
response = opener.open(request)

print response.info()