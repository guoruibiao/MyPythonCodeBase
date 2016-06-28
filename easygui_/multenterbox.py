# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ =  为用户提供多个简单的输入框，要注意以下几点：\
                # 如果用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户为输入的选项。\
                # 如果用户输入的值比选项多的话，则返回的列表中的值将截断为选项的数量。\
                # 如果用户取消操作，则返回域中的列表的值或者None值。\'

import easygui
msg = '提供的多个简单的输入框'
title = '可以输入多个选项的输入框'
fields = ('A','B','C','D',)
values=('杨贵妃','昭君','西施','小乔',)
ls = easygui.multenterbox(msg,title,fields,values)
for item in ls:
    print item

"""
D:\Software\Python2\python.exe E:/Code/Python/MyTestSet/easygui_/multenterbox.py
杨贵妃
昭君
西施
小乔

Process finished with exit code 0

"""