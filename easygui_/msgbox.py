# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ =  一个最简单的类似于Java的MessageBox的小窗口

import easygui
title = easygui.msgbox(msg='提示信息',title='标题部分',ok_button="OOK")

msg = easygui.msgbox('Hello Easy GUI')
print '返回值：' + msg

ccbox = easygui.ccbox("here is Continue | Cancel Box!")
print '返回值：' + str(ccbox)

ynbox = easygui.ynbox("Yes Or No Button Box!")
print '返回值： ' + str(ynbox)
