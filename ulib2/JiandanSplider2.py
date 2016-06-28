# coding:UTF-8

# 导入我们需要的网络模块，正则表达式模块，以及产生随机数的模块
import urllib2,urllib,re,random

# 根据传入的URL网址，获得该网址对应的全部的html页面（纯网页，并没有做任何的解析）
def getHtml(url,headers) :
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    page = response.read()
    return page

# 根据之前获得那个url对应的网页信息，将这张网页里面包含的所有的含有<img src=".+\.jpg"/>的url存储到一个列表中
def getImageUrls(page):
    reg = r'src="(.+?\.jpg)"'
    imageReg = re.compile(reg)
    img_urls = re.findall(imageReg,page)
    return img_urls

# 这是个测试的方法，并没有实际的价值。列出来的目的只是为了纪念一下，最终功能实现的这个过程，仅此！
# def getTotalImageUrls(original_url,headers):
#     totalImageUrls = []
#     for item in range(1980, 1990):
#         original_url += original_url + str(item)
#         page = getHtml(original_url,headers)
#         images_url = getImageUrls(page)
#         totalImageUrls.append(images_url)
#         return totalImageUrls

# 根据给定的路径，文件名，将指定的数据（这里是一张图片，是的。一张图片）写入到文件中。需要注意的是每次都需要关闭file
def writeToFile(path,name,data):
    file = open(path+name,'wb')
    file.write(data)
    file.close()
    print name+" has been Writed Succeed!"

# 下载图片，并且调用刚才的  writeToFile(path,name,data): 函数。将图片直接写到对应的路径下面
# 这里借助于一个random模块，为了产生图片之间尽量不重复的文件名，以防止文件的覆盖或者出现其他的问题
def downloadImages(images_url,path,headers) :
    for i, item in enumerate(images_url):
        everypicture = getHtml(item,headers)
        # 此处下载之后的文件使用了item来命名是为了避免图片的覆盖
        writeToFile(path, str(i+random.randint(1,100000000)) + ".jpg", everypicture)


# 提供单个url网址内图片的下载
def singleImageDownload(outputPath,targeturl,headers) :
    originalurl = targeturl
    page = getHtml(originalurl,headers)
    images_url = getImageUrls(page)
    downloadImages(images_url,path,headers)




# 提供批量下载的函数，对未成功下载的提示未成功下载语句
def batchImageDownload(outputPath, originalurl, headers, start, end):
    for item in range(2000, 4000):
        try:
            originalurl = 'http://bizhi.souutu.com/mnbz/' + str(item) + '.html'
            page = getHtml(originalurl)
            images_url = getImageUrls(page)
            downloadImages(images_url,headers)
        except:
            print str(item) + str(' web site cannot be spidered! Sorry!')
            continue


# --------------------------------------------------------------------------------------------------
# 下面是我们的测试代码,仅仅拿单个url页面做了个测试，亲测好使


headers = {
    'referer':'http://desk.zol.com.cn/bizhi/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}

path = "F:\\pachong\\samoye\\"
url = 'http://desk.zol.com.cn/bizhi/6317_77829_2.html'
singleImageDownload(path,url,headers)