# coding:UTF-8

from bs4 import BeautifulSoup
'''
BeautifulSoup 将复杂的HTML文档转化成一个复杂的树形结构，每个节点都是
Python对象，所有对象可以归纳为4种：
Tag                                 标签相关
NavigableString                     标签内部的文本信息
BeautifulSoup                       表示一个文档的所有的内容，包含了上面那两个
Comment                             特殊的NavigableString对象，输出的内容不包括注释字段
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

print '获取为Tag对象类型的测试：---------------------------------------------------------------------\n'
print soup.title.text
print soup.a.text

print '下面是使用tag标签属性来输出的结果：\n'
print soup.name
print soup.head.name
print soup.p.attrs
print soup.p['class']

print '下面是使用get方式来获取标签中的相关的信息：\n'
print soup.p.get('class')
print soup.p.get('name')

print '除了获取这些信息之外，还可以使用代码进行相关的修改（不过只是内存中的修改，而不是文件的修改）：\n'
soup.p['class'] = 'mark'
print soup.p.get('class')


print '获取为NavigableString对象类型的测试：---------------------------------------------------------------------\n'
print soup.p.string
print soup.a.string


print '获取为BeautifulSoup对象类型的测试：---------------------------------------------------------------------\n'
print soup.p.name
print soup.p.attrs


print '获取为Comment对象类型的测试：---------------------------------------------------------------------\n'
print soup.a
print soup.a.string
