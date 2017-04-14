# coding: utf8

# @Author: 郭 璞
# @File: crawl.py                                                                 
# @Time: 2017/4/14                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 爬取相关于Linux command的使用手册信息

import requests
from bs4 import BeautifulSoup
import re
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"
}


def getCommandList():
    """
    获取Linux Command 列表
    :return:
    """
    url = 'http://cnajiu.cn/'
    html = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    lists = soup.find_all('a', {'class': 'weui-cell_link col-5'})
    # 其实还可以通过a标签进行解析，直接得到本网站的相关用户手册信息。但是这个网站的手册做的不够好，我这里只是存储一下都有那些命令罢了。
    return [item.get_text() for item in lists]


def stripHtml(html):
    data = re.sub('<.*?>', '', html)
    data = re.sub("</.*?>", '', data)
    data = data.strip('\n').strip('\t').strip('\r').strip('\n')
    return data

def safeget(data):
    try:
        data = data if data is not None else "待更新"
        data = ''.join([str(item) for item in data])
        data.strip('\n').strip('\t')
        data = re.sub("\"", '&quot;', data)
        return stripHtml(data)
    except Exception as e:
        print(e)
        return "数据正在加载... ..."
##############################################################

def parser(name):
    """
    应先对name的合法性进行判断。可以通过对网页内容的获取成功与否来间接实现。
    :param name:
    :return:
    """
    url = 'http://man.linuxde.net/{}'.format(name)
    try:
        response = requests.get(url=url, headers=headers)
        statuscode = response.status_code
        if statuscode == 200:
            html = response.text
        else:
            print("命令不合法，或者关于该命令的手册还未收录！")
    except:
        pass
    ## 解析网页，获取内容
    try:
        soup = BeautifulSoup(html, 'html.parser')
        type = safeget(soup.find('div', {'class': "tag f_yh r"}).get_text())  # 因为网页上只有这一个样式，所以可以直接用find实现
        name = safeget(soup.find('div', {'class': 'post_hd clearfix'}).h1.get_text())
        post = soup.find('div', {'class': 'post_bd post'})
        description = safeget(post.find_all('p')[0].get_text())
        syntax = safeget(post.find_all('pre')[0].get_text())
        options = safeget(post.find_all('pre')[1].get_text())
        params = safeget(post.find_all('p')[1].get_text())
        examples = safeget(post.find_all('pre')[1].find_next_siblings()[4:])

        # 为了方便使用这些值，使用一个对象进行保存
        item = {
            'name': name,
            'type': type,
            'description': description,
            'syntax': syntax,
            'options': options,
            'params': params,
            'examples': examples
        }
        print(json.dumps(item))
    except Exception as e:
        print("parse过程： ", e)


if __name__ == '__main__':
    print("目前可以提供的查询命令为：")
    lists = getCommandList()
    for index in range(len(lists)):
        if (index+1) %10 == 0:
            print(end='\n')
        else:
            print(lists[index], end='\t')
    print()

    parser(input('请输入您想要查找的命令的名称：'))
