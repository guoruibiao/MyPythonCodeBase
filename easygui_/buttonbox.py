# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 能让你最初选择的简单的界面，第二个参数为一个列表

import easygui

# choice = easygui.buttonbox("这里是提示的语句信息：\n", title='三选一', choices=['one' \
#     , 'two', 'three'])
# easygui.msgbox('您选择了：' + str(choice))
#
# # choices 内只能有两个参数 ，选择哪一个将返回1，否则返回0
# bool = easygui.boolbox('msg提示信息', title='标题部分', choices=['A', 'B'])
# easygui.msgbox(bool)

image = 'me.jpg'
msg = 'Here is my photo,a python fan also'
choices = ['Yes','No',"Not Sure"]
title = 'Am I handsome?'
easygui.buttonbox(msg,title,image=image,choices=choices)