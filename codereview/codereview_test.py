# coding: utf8

# @Author: 郭 璞
# @File: codereview_test.py
# @Time: 2018/2/25                                   
# @Contact: 1064319632@qq.com
# @blog: http://blog.csdn.net/marksinoberg
# @Description: 创建一个 用于代码review的gist
import requests

url = "http://47.94.19.186/codereview/addreview.php"
content = """
Modified: README.md
 =================================================================== ---
 README.md 2018-02-25 02:59:01 UTC (rev 76) +++ README.md 2018-02-25 09:39:25
 UTC (txn 76-2o) @@ -18,6 +18,7 @@ ## 提交注意 提交代码的命令为： `svn commit xxx.yyy -m
 "说明文本"`， **提交信息的长度已经加了限制，不应该少于10个字符长度:** +--- 提交之前尽量做到规范一点哈。 -
 说明文本，一般来说要简明扼要，描述下提交了什么，或者提交的文件有什么作用就可以了。 Modified: introduction.txt
 =================================================================== ---
 introduction.txt 2018-02-25 02:59:01 UTC (rev 76) +++ introduction.txt
 2018-02-25 09:39:25 UTC (txn 76-2o) @@ -1,4 +1,4 @@ -工程编号 100
 +﻿工程编号 100
 
 模块编号
 
 @@ -10,4 +10,6 @@ 
 研究生导师 104
 
 - 企业 105 \ No newline at end of file
 + 企业 105
 +
 +-------------------------- \ No newline at end of file
"""
payload = {
  "author": "biaobiao",
  "version": 75,
  "content": content,
  "commitmsg": "测试下code review 服务"
}

response = requests.post(url, data=payload)
print(response.status_code)
print(response.text)