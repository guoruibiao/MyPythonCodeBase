# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/10/10'
#    __Desc__ = crawl the top 20 movies in douban

# 爬取，处理网络数据相关
import json
import urllib2

# 用来提取某一个群中的qq号码
import re

# 邮件发送相关
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# mako模板相关
from jinja2 import Template

# 通过随机数模块设置不定时的休眠
from time import *
from random import randint

#######################################################################################################################
## 创建几个相关的类，方便赋值

class Movie(object):
    """电影对象"""
    def __init__(self, average=0, stars=0, genres=[], title='', original_title='', avatars=[], directors=[], image=''):
        self.average = average
        self.stars = stars
        self.genres = genres
        self.title = title
        self.original_title = original_title
        self.avatars = avatars
        self.directors = directors
        self.image = image

    def __getitem__(self, item):
        return self.title



class Avatar(object):
    """演员对象类"""
    def __init__(self, name='',photo=''):
        self.name = name
        self.photo = photo

    def __getitem__(self, name):
        return self.name

class Director(object):
    """导演类"""
    def __init__(self, name='', photo=''):
        self.name = name
        self.photo = photo

    def __getitem__(self, name):
        return self.name

########################################################################################################################




# 使用urllib2模块可以模拟浏览器方式爬取或者获取数据，增强型的访问
def getJson(url):
    # 构造浏览器的头部信息
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
    req = urllib2.Request(url=url, headers=header)
    # 读取接口返回的JSON数据，并转换成字典之后。返回。
    data = json.loads(urllib2.urlopen(req).read())
    return data

# 将字典数据中固定格式的数据库分割成列表
def parse2list(jsondata={}):
    ls = []
    ls = jsondata['subjects']
    return ls

# 字典数据根据键值对的关系存储到刚才的类对象实例中，期间可能会有些数据报错，故采用try块处理掉
def json2obj(data):
    try:
        average = data['rating']['average']
        stars = data['rating']['stars']
        genres = data['genres']
        title = data['title']
        original_title = data['original_title']
        image = data['images']['large']

        # 获取演员的信息
        avatars = []
        for item in range(len(data['casts'])):
            avatar_photourl = data['casts'][item]['avatars']['medium']
            avatar_name =  data['casts'][item]['name']
            avatar = Avatar(name=avatar_name, photo=avatar_photourl)
            avatars.append(avatar)

        # 获取导演的信息
        directors = []
        for item in range(len(data['directors'])):
            director_photourl = data['directors'][item]['avatars']['medium']  if type(data['casts'][item]['avatars']['medium'])!=None else 'http://www.douban.com'
            director_name = data['directors'][item]['name']
            director = Director(name=director_name, photo=director_photourl)
            directors.append(director)

        # 组装电影信息，并返回
        movie = Movie(average=average, stars=stars, genres=genres, title=title, original_title=original_title, avatars=avatars, directors=directors, image=image)
    except Exception as e:
        print 'error:%s'%e
    print movie.directors, movie.avatars
    # 将一个Subject生成的Movie对象实例返回
    return movie


# 将网络上获取到的列表形式的数据块转换成movie对象的列表中，方便接下来的模板使用
def json2movies(jsondata):
    movies = []

    for item in jsondata:
        try:
            # 将每一个数据块转换成一个Movie对象
            movieobj = json2obj(item)
            movies.append(movieobj)
        except Exception:
            continue

    # 返回的是包含了所有的数据的电影列表
    return movies

# 采用jinja2模板技术，生成待会用于发邮件的html文件
def renderhtml(htmlpath, movies):
    # 读取html模板文件
    htmlfile = open(htmlpath, 'rb')
    htmlline = htmlfile.read()
    htmlfile.close()

    # 使用模板技术，将变量赋值给模板，让模板进行处理
    t = Template(htmlline)
    # 模板底层会帮助，进行渲染操作
    renderedhtml = t.render(movies=movies)


    # 将渲染好的html文件写回到待发送列表
    renderdfile = open(r'./renderd.html', 'wb')
    renderdfile.write(renderedhtml)
    renderdfile.close()
    print 'render success'


# 根据QQ群导出的txt文件，使用正则表达式提取出近期发言人的QQ号，然后附加上@qq.com组建成QQ邮箱，并进行去重处理
def getemails(chatfile):
    file = open(chatfile, 'rb')
    data = file.read()
    file.close()

    reg = r'(\d{9,10})'
    # list(set(ls))就是借助set的不重复性质来去重
    ls = list(set(re.findall(reg, data)))

    emails = []
    for item in ls:
        emails.append(str(item) + str("@qq.com"))
    return emails

# 发送邮件，由于message['to']处出现问题，这里只能一次发一个了，按照原理是可以群发的。
def sendbyemail(sender='', password='', movies=None, receivers=[]):

    # 设置一下发邮件的信息

    sender = sender
    password = password

    # 为每一个邮箱发送邮件
    for receiver in receivers:

        # 不定时的休眠一下，防止因发信频率过快而导致的系统退信的情况发生
        sleep(randint()*7)

        # 开始构造要发送的数据
        # 三个参数：第一个为纯文本，第二个plain设置文本格式，第三个为编码格式
        text = open(r'./renderd.html', 'rb').read().encode('utf8')

        message = MIMEText(str(text), 'html', 'utf-8')
        # message['From'] = Header('Hail Studio', 'utf-8')
        # message['To'] = Header('HailStudio VIP客户', 'utf-8')
        message['from'] = sender
        message['to'] = receiver

        subject = '爬虫测试：即将上映的top20电影详情 '
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect('smtp.163.com', 25)
            smtpObj.login(sender, password)
            smtpObj.sendmail(sender, receiver, message.as_string())
            smtpObj.quit()

            print '邮件已成功发送了Success!'
        except smtplib.SMTPException as e:
            print  '邮件发送失败了Failed！', e









if __name__ == '__main__':

    url = 'http://api.douban.com/v2/movie/coming_soon'
    data = getJson(url)
    subjects = parse2list(data)
    movies = json2movies(subjects)
    renderhtml(r'./template.html', movies)

    # send email QQ群聊天记录必须导出，否则正则表达式无法正常的运行
    chatpath = r'./qqqun.txt'
    receivers = getemails(chatpath)
    sender = '邮箱'
    password = '密码'
    sendbyemail(sender=sender, password=password, movies=movies, receivers=receivers)

