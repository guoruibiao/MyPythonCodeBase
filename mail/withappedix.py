# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/26'
#    __Desc__ = 实现发送带有各种附件类型的邮件

import urllib, urllib2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = '15640863027@163.com'
password = 'guoruibiao285514'
sender = username
receivers = ','.join(['1064319632@qq.com'])

# 如名字所示： Multipart就是多个部分
msg = MIMEMultipart()
msg['Subject'] = 'Python mail Test'
msg['From'] = sender
msg['To'] = receivers

# 下面是文字部分，也就是纯文本
puretext = MIMEText('我是纯文本部分，')
msg.attach(puretext)

# 下面是附件部分 ，这里分为了好几个类型

# 首先是xlsx类型的附件
xlsxpart = MIMEApplication(open('test.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename='test.xlsx')
msg.attach(xlsxpart)

# jpg类型的附件
jpgpart = MIMEApplication(open('beauty.jpg', 'rb').read())
jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
msg.attach(jpgpart)

# mp3类型的附件
mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
msg.attach(mp3part)

##  下面开始真正的发送邮件了
try:
    client = smtplib.SMTP()
    client.connect('smtp.163.com')
    client.login(username, password)
    client.helo()
    client.sendmail(sender, receivers, msg.as_string())
    client.quit()
    print '带有各种附件的邮件发送成功！'
except smtplib.SMTPRecipientsRefused:
    print 'Recipient refused'
except smtplib.SMTPAuthenticationError:
    print 'Auth error'
except smtplib.SMTPSenderRefused:
    print 'Sender refused'
except smtplib.SMTPException,e:
    print e.message
