# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/26'
#    __Desc__ = 收邮件，缺点是只检测一次

import poplib
import base64
from email import parser

mailserver = 'pop.163.com'
username = '15640863027'
password = 'guoruibiao285514'
try:
    pop_conn = poplib.POP3_SSL(mailserver)
    pop_conn.user(username)
    pop_conn.pass_(password)

    # # 开始从服务器端获取数据
    # messages = [pop_conn.retr(i) for i in range(1,len(pop_conn.list()[1])+1)]
    #
    # # 将数据拼接起来
    # messages = ['\n'.join(mssg[1]) for mssg in messages]
    #
    # # parse message into an email object
    # messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    # for item in messages:
    #     print base64.decode(item['Subject'],'utf-8')
    #
    # pop_conn.quit()
    server = poplib.POP3(mailserver)
    print server.getwelcome()

    server.user(username)
    server.pass_(password)
    print 'Message:%s size %s'%server.stat()
    resp, mails , octets  = server.list()
    print mails

    # 获取最新的一封，任意索引号从1开始
    index = len(mails)
    resp,lines,octets = server.retr(index)
    msg_content = '\r\n'.join(lines)
    msg = parser.Parser().parsestr(msg_content)
    print msg
    server.quit()
except Exception,e :
    print e
