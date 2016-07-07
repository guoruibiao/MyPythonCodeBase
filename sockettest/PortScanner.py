# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/7'
#    __Desc__ =  端口扫描工具

import socket
import optparse
from socket import *

def connScan(tagHost,tagPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tagHost,tagPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        print '[+]%d/tcp open'%tagPort
        print '[+] ' + str(results)
    except:
        print '[-] %d/tcp closed'%tagPort

def portScan(tagHost , tagPorts):
    try:
        tagIP = gethostbyname(tagHost)
    except:
        print '[-] Cannot resolve %s : Unknown host'%tagHost
        return
    try:
        tagName = gethostbyaddr(tagIP)
        print '\n[+] Scan Results for:'+ tagName[0]
    except:
        print '\n[+] Scan Results for:' + tagIP

    setdefaulttimeout(2)
    for tagPort in tagPorts:
        print 'Scanning port ' + tagPort
        connScan(tagHost,tagPort)

def main():
    parser = optparse.OptionParser("Usage%prog -H <tagget Host> -p <target port>")
    parser.add_option('-H',dest='tagHost',type='string',help='sepcify target host')
    parser.add_option('-p',dest='tagPorts',type='string',help='specify port!')
    (options,args) = parser.parse_args()
    tagHost = options.tagHost
    tagPorts = str(options.tagPorts).split(', ')
    if (tagHost == None) | (tagPorts[0] == None):
        print '[-] You must specify a target host and port[s].'
        exit(0)
        portScan(tagHost,tagPorts)

if __name__ == "__main__":
    main()

