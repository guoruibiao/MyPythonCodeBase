# coding:UTF-8
#引入urllib库
import urllib
def getHTML(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html

