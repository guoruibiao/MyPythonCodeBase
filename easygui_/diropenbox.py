# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 该函数用于提供一个对话框，返回用户选择的目录名，该目录名是带有完整的路径的
# 选择Cancel的话返回值默认为None

import easygui

msg = '选择一个文件，将会返回该文件的完整的目录哦'
title = ' 文件选择对话框'
default = r'F:\flappy-bird'
full_file_path = easygui.diropenbox(msg, title, default)
print '选择的文件的完整的路径为：' + str(full_file_path)


# D:\Software\Python2\python.exe E:/Code/Python/MyTestSet/easygui_/diropenbox.py
# 选择的文件的完整的路径为：F:\flappy-bird
#
# Process finished with exit code 0