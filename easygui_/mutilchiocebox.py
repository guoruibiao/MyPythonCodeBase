# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 一个多选的列表项.呵呵了，这个版本貌似有问题。我的多选并没有真正的实现

import easygui

msg = '选择此列表项中你喜欢的一个吧'
title = '必须选择一个哦'
choices = (1,2,3,4,5,6,7,8,9)
answer1 = easygui.multchoicebox(msg,title,choices)
for item in answer1:
    print item