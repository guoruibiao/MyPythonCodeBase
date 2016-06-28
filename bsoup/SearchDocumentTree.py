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

# --------------------------------find_all中使用name参数----------------------------------------------------------------
# 传入的参数为字符串的时候
for item in soup.find_all('a'):
    print item

# 传入的参数为正则表达式的时候
import re
for item in soup.find_all(re.compile("^b")):
    print item

# 传进来的参数是一个列表
for item in soup.find_all(['a','b']):
    print item

# --------------------------------find_all中使用keyword参数-------------------------------------------------------------
print soup.find_all(id='link2')
print soup.find_all(href=re.compile('elsie'))
# 使用class关键字进行匹配的时候要加上一个下划线，这样才不会与Python的关键字冲突
print soup.find_all(class_='title')

# --------------------------------find_all中使用text参数----------------------------------------------------------------
print soup.find_all(text=r'Tillie')
print soup.find_all(text=['Tillie','Elsie','Lacie'])


# ---------------------------------还可以使用CSS的三种方式进行获取------------------------------------------------------
'''
soup.select('.class_name')
soup.select('#id_value')
或者组合方式查找
soup.select('p #line1')
通过子标签查找
soup.select('head > title')

通过属性查找:注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到
soup.select('a[class="class_name"]')
print soup.select('a[href="http://example.com/elsie"]')
'''
# 以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() /.text方法来获取它的内容。
print type(soup.select('title'))
print soup.select('title')[0].get_text()
for title in soup.select('title'):
    print title.get_text()