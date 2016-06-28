# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/6/24'
#    __Desc__ = 简单的入门示例程序
import pyHook
import pythoncom
from time import *

result = ''

def onMouseEvent(event):
    # 监听鼠标事件
    print "Message Name :", event.MessageName
    print "Message:",event.Message
    print "Time: " , event.Time
    print "Window: ",event.Window
    print "Window Name : " ,event.WindowName
    print "Position : ",event.Position
    print "Wheel : ",event.Wheel
    print "Injected: ",event.Injected

    # 需要注意的是返回True，以便将事件传给其他的处理程序，如果返回False的话，鼠标事件在这里就会被拦截，即鼠标会僵在此处失去响应
    return True

def onKeyboardEvent(event):
    # 监听键盘事件
    print "MessageName:", event.MessageName
    print "Message:", event.Message
    print "Time:", event.Time
    print "Window:", event.Window
    print "WindowName:", event.WindowName
    print "Ascii:", event.Ascii, chr(event.Ascii)
    print "Key:", event.Key
    print "KeyID:", event.KeyID
    print "ScanCode:", event.ScanCode
    print "Extended:", event.Extended
    print "Injected:", event.Injected
    print "Alt", event.Alt
    print "Transition", event.Transition
    print "---"
    # 同鼠标事件监听函数的返回值
    # 写一个保存到本地文件的方法,而且应该以写二进制的方式来写入,设置result为全局的，避免文件被覆盖
    global result
    file = open(r'F:/log.txt','wb')
    result = result + "Time : " + str(asctime())+"|:"+"WindowName:"+str( event.WindowName)+"|"+"Key:"+str( event.Key)+"|"+"MessageName:"+str( event.MessageName)
    file.writelines(result)
    if event.Key == "q":
        file.close()
    return True

def main():
    # 创建一个：钩子“管理对象
    hm = pyHook.HookManager()
    # 监听所有的键盘事件
    hm.KeyDown = onKeyboardEvent
    #设置键盘”钩子“
    hm.HookKeyboard()
    # 监听鼠标事件
    hm.mouseAll = onMouseEvent
    # 设置鼠标钩子
    hm.HookMouse()
    # 进入循环侦听，需要手动进行关闭，否则程序将一直处于监听的状态。可以直接设置而空而使用默认值
    pythoncom.PumpMessages()
    # 我也不知道为什么直接放置到main函数中不管用

if __name__ == "__main__":
    main()