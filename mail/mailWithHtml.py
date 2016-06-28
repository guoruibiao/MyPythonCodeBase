# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 实现一个带有html文件的邮件发送
import smtplib
from email.mime.text import MIMEText
from email.header import Header



"""
请确保自己的邮箱的smtp协议开启，都则会出现认证的错误的，如ssh等
"""


sender = "15640863027@163.com"
# 收件人，可以是多个
receivers = ['1064319632@qq.com']

# 三个参数：第一个为纯文本，第二个plain设置文本格式，第三个为编码格式
htmlContent = open('index.html','r').read()
message = MIMEText(htmlContent,'html','utf-8')
message['From'] = Header('来自Mark','utf-8')
message['To'] = Header('测试标题','utf-8')

subject = '哈哈哈哈哈哈，这是邮件的主题 '
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('smtp.163.com',25)
    smtpObj.login(sender,'guoruibiao285514')
    smtpObj.sendmail(sender,receivers,message.as_string())
    smtpObj.quit()
    print '邮件已成功发送了'
except smtplib.SMTPException,e:
    print  e.message


