# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = 该函数提供了一个对话框，让用户选择文件需要保存的路径（带完整的路径）选择Cancel返回None
#               default 参数应该包含一个文件名（例如当前需要保存的文件名），当然你也可以设置为空的，或者包含一个文件格式掩码的通配符。
#               filetypes参考如上面的fileopenbox

import easygui

msg = 'Save your file'
title = "to Save File"
default = 'E:/Code/Python/MyTestSet/easygui/newFile.*'
savedfile = easygui.filesavebox(msg,title,default)
print savedfile
print '当然了，这里仅仅是一个完整的路径加上文件名而已，并不会真的保存成一个文件，保存文件需要用到其他的库'



# D:\Software\Python2\python.exe E:/Code/Python/MyTestSet/easygui_/filesavebox.py
# E:\Code\Python\MyTestSet\easygui_\newFile.doc
# 当然了，这里仅仅是一个完整的路径加上文件名而已，并不会真的保存成一个文件，保存文件需要用到其他的库
#
# Process finished with exit code 0
