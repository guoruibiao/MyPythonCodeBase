# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header



"""
请确保自己的邮箱的smtp协议开启，都则会出现认证的错误的，如ssh等
"""


sender = "15640863027@163.com"
# 收件人，可以是多个
receivers = ['3126969188@qq.com']

# 三个参数：第一个为纯文本，第二个plain设置文本格式，第三个为编码格式
message = MIMEText('System.out.println("你是猴子请来的逗比不？\n")。Pure Text Here!','plain','utf-8')
message['From'] = Header('来自《太阳的后裔》','utf-8')
message['To'] = Header('Py','utf-8')

subject = '呵呵，不就是一个主题嘛 '
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

