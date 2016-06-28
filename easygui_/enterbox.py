# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 可以满足用户输入的控件

import easygui

st = easygui.enterbox("请输入一段文字：\n")
print "您输入了：  " + str(st)
