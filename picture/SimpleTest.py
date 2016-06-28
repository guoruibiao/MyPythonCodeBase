# coding:UTF-8
# 导入相关的模块，用以快速的进行使用库文件
import urllib  # 对于下载网页的时候用到的库
import sys # 格式化输出时用到的库
import re  # 正则表达式的库
import os  # 文件操作的库

# 根据给定的URL，获得一张完整的网页内容
def getHtml(url):
    reload(sys)
    return urllib.urlopen(url).read()

# 根据给定的路径，文件名，将指定的数据写入到文件中
def writeToFile(path,name,data):
    file = open(path+name,'wb')
    file.write(data)
    file.close()
    print name+" has been Writed Succeed!"

#url = "http://www.10danteng.com/index/pages/id/11036/"
# 从一张完整的网页中使用正则表达式匹配的方式返回一个图片URL的列表
def getImageLists(page):
    reg =re.compile(str( r'src="(.+?\.jpg)"'))
    images_url = re.findall(reg,page)
    return images_url
# --------------------------------------------------------------------------------------------------
# 下面是我们的测试代码
name = 'me'
path = "F:\\pachong\\"
url = 'http://www.u148.net/article/55557.html'
page = getHtml(url)
images_url = getImageLists(page)
#writeToFile(path,str(name)+".jpg",content)
for i, item in enumerate(images_url):
    everypicture =  getHtml(item)
    writeToFile(path,str(i)+".jpg",everypicture)