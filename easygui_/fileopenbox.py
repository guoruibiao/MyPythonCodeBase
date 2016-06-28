# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 此方法用于提供一个对话框，返回用户选择的文件名，带有完整的路径，选择Cancel返回None
#              default="c:/fishc/*.py" 即显示 C:\fishc 文件夹下所有的 Python 文件。
#              default="c:/fishc/test*.py" 即显示 C:\fishc 文件夹下所有的名字以 test 开头的 Python 文件。
#              filetypes参数是包含文件掩码的字符串的列表，记住是个列表。如：filetypes = ["*.css", ["*.htm", "*.html", "HTML files"]]

import easygui

msg = '返回选择的文件的完整的路径，选择Cancel则返回None'
title = '文件选择器'
default = 'E:/Code/Python/MyTestSet/easygui/*.py'

opened_files = easygui.fileopenbox(msg,title,default,multiple=True)
for item in opened_files:
    print item



# D:\Software\Python2\python.exe E:/Code/Python/MyTestSet/easygui_/fileopenbox.py
# E:\Code\Python\MyTestSet\easygui_\me.jpg
# E:\Code\Python\MyTestSet\easygui_\buttonbox.py
# E:\Code\Python\MyTestSet\easygui_\choicesbox.py
# E:\Code\Python\MyTestSet\easygui_\diropenbox.py
# E:\Code\Python\MyTestSet\easygui_\enterbox.py
# E:\Code\Python\MyTestSet\easygui_\fileopenbox.py
# E:\Code\Python\MyTestSet\easygui_\integerbox.py
#
# Process finished with exit code 0

