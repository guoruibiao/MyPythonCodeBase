# coding:utf-8
import json
import urllib2
import urllib

import re
from bs4 import BeautifulSoup
import config
import sys
import cookielib

def getContent():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    cookie = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    url = config.login_url
    headers = config.login_header
    data = urllib.urlencode(config.login_data)
    request = urllib2.Request(url, data, headers)
    response = opener.open(request).read()

    request=urllib2.Request(config.course_url,None,config.course_header)
    response=opener.open(request).read()

    page_html = unicode(response, 'gb2312').encode('utf-8')
    f=open('page.html','w')
    f.write(page_html)
    f.close()


    f = open('page.html', 'r')
    page_html = f.read()
    f.close()

    soup = BeautifulSoup(page_html, 'html.parser', from_encoding='utf-8')
    display_tag = soup.find_all('table', class_='displayTag')
    course_table = display_tag[0]
    rows = course_table.find_all('tr')

    rows.pop(10)
    rows.pop(5)
    rows.pop(0)

    table_info = []
    for tr in rows:
        tds = tr.find_all('td')
        for td in tds:
            # print 'td ',td
            if td.p:
                info = td.p.string
            else:
                info = str(td.contents[0].string)
            pattern = re.compile(r'\s| +')
            info = re.sub(pattern, '', str(info))
            table_info.append(info)

    course = []
    for i in range(12):
        section = {
            'section': table_info[8 * i + i / 4 + 1],
            'classes': table_info[8 * i + i / 4 + 2: 8 * i + i / 4 + 9]
        }
        course.append(section)

    json_text = json.dumps(course, ensure_ascii=False)
    #print json_text
    return json_text

if __name__ == "__main__" :
    print getContent()