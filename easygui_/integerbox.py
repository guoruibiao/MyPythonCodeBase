# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 提供给用户简单的输入框，只能是给定的数字的范围

import easygui

msg = '请输入一个数字，范围在0-100'
title = '限制为数字类型'
lowerbound = 0
upperbound = 100
default = ''
image = 'me.jpg'
result = easygui.integerbox(msg,title,default,lowerbound,upperbound,image)
print result

