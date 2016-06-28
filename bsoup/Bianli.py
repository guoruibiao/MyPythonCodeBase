# coding: UTF-8

from bs4 import BeautifulSoup

'''
BeautifulSoup 完成HTML文档遍历的操作

'''

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# 第二个参数作为解析器而存在！ 有html.parser;lxml;html5lib等等解析方式
soup = BeautifulSoup(html,'lxml')
# 还可以使用本地的html文件
# soup = BeautifulSoup(open('file.html'))


# 遍历所有名称为head的直接子节点，也就是只有一个
print soup.head.contents

# 遍历所有的子节点，返回值是 以列表存在
for child in  soup.body.children:
    print child

for item in soup.body.descendants:
    print item

# 获得节点的内容，仍然是使用.string 的方式.返回值是一个内容；如果想获取多个的话，就是用.strings或者.stripped_strings
print soup.a.string
print soup.a.strings
print soup.a.stripped_strings

# 与此类似的还有获取父节点，获取所有的父节点，获得兄弟节点，获取前一个节点以及获取后一个节点等等
