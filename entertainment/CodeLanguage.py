# coding:UTF-8

'''
Python创始人，java创始人图像下载

'''

import urllib,urllib2, re

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

def getImageUrls(content):
    reg = r'src="(.+?\.jpg)"'
    imgreg = re.compile(reg)
    imageurls = re.findall(imgreg,content)
    return imageurls

def writeToFile(path,filename,data):
    file = open(path+'\\' + str(filename) +'.jpg','wb')
    file.write(data)
    file.close()
    print 'File Writed Success!'

# 程序运行入口
if __name__ == "__main__":

    url = 'http://www.open-open.com/news/view/16810c3'
    path = "F:\\pachong\\codelanguage"
    data = getHtml(url)
    imgurls = getImageUrls(data)
    for index,item in enumerate(imgurls):
        tempdata = getHtml(item)
        writeToFile(path,index,tempdata)
        print index,'下载完毕！'
    print '工程download Over！'