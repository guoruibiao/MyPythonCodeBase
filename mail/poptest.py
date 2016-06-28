# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/26'
#    __Desc__ = 使用poplib试下python接收邮件

import os, sys, string
import poplib


# pop3服务器地址
host = "pop3.163.com"
# 用户名
username = "15640863027@163.com"
# 密码
password = "guoruibiao285514"
try:
    # 创建一个pop3对象，这个时候实际上已经连接上服务器了
    pp = poplib.POP3(host)
    # 设置调试模式，可以看到与服务器的交互信息
    pp.set_debuglevel(1)
    # 向服务器发送用户名
    pp.user(username)
    # 向服务器发送密码
    pp.pass_(password)
    # 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节
    ret = pp.stat()
    print ret
    # 需要取出所有信件的头部，信件id是从1开始的。
    for i in range(1, ret[0] + 1):
        # 取出信件头部。注意：top指定的行数是以信件头为基数的，也就是说当取0行，
        # 其实是返回头部信息，取1行其实是返回头部信息之外再多1行。
        mlist = pp.top(i, 0)
        print 'line: ', len(mlist[1])
    # 列出服务器上邮件信息，这个会对每一封邮件都输出id和大小。不象stat输出的是总的统计信息
    ret = pp.list()
    print ret
    # 取第一封邮件完整信息，在返回值里，是按行存储在down[1]的列表里的。down[0]是返回的状态信息
    down = pp.retr(1)
    print 'lines:', len(down)
    # 输出邮件
    for line in down[1]:
        print line
    # 退出
    pp.quit()
except Exception , e:
    print e
