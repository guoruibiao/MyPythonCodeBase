# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/5/25'
#    __Desc__ = easygui 还提供了对大量文本的支持，以及对代码文本的支持

import easygui

msg = '大文本的支持'
title = 'Text Code'
text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJIKLMNOPQRSTUVWXYZ0123456789-/'
textContent = easygui.textbox(msg,title,text)
codeContent = easygui.codebox(msg,title,)
print textContent
print codeContent

# D:\Software\Python2\python.exe E:/Code/Python/MyTestSet/easygui_/text_codebox.py
# abcdefghijklmnopqrstuvwxyzABCDEFGHJIKLMNOPQRSTUVWXYZ0123456789-/
# public class HelloWorld{
# 	public static void main(String []args) {
# 		System.out.println("Hello World!");
# 	}
# }
#
# Process finished with exit code 0
