#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = '15640863027@163.com'  
receiver = '1064319632@qq.com'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '15640863027'  
password = 'PRCstylewarmup'  
  
msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit() 