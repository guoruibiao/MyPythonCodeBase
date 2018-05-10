# coding: utf8

# @Author: 郭 璞
# @File: codereview_get.py                                                                 
# @Time: 2018/2/25                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 
import requests

url = "http://47.94.19.186/codereview/getreview.php"
payload = {
    "landmarkversion": 75,
    "id": 1519555078
}
response = requests.post(url, data=payload)
print(response.status_code)
print(response.text)