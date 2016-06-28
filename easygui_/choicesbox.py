# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 从一个列表中选择其中的一个，会有返回值的出现

import easygui

msg = '选择此列表项中你喜欢的一个吧'
title = '必须选择一个哦'
choices = ['1','2','3','4','5','6','7']
answer = easygui.choicebox(msg,title,choices)
print '你选择了 ：' + str(answer)