# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 这是一个很好用的对话框，当应用程序出现异常的时候，就可以通过这个来给与用户友好的界面提示

import easygui

try:
    int('Exception')
except:
    easygui.exceptionbox('int类型数据转换错误！请检查您的数据类型！')

# 会弹出一个界面，内容信息可以自己定义，如上面。下面的内容就是追踪到的出错信息
# Traceback (most recent call last):
#   File "E:/Code/Python/MyTestSet/easygui_/exceptionbox.py", line 10, in <module>
#     int('Exception')
# ValueError: invalid literal for int() with base 10: 'Exception'
