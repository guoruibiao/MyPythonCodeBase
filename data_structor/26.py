# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/1'
#    __Desc__ = 使用Tkinter画同心圆

def circle(width=800,height=600,bg='green'):
    from Tkinter import *
    # 确定画布信息
    canvas = Canvas(width=width,height=height,bg=bg)
    canvas.pack(expand=YES,fill=BOTH)

    k = 1
    j = 1
    # 确定圆的个数
    for index in range(0,32):
        # 画圆需要提供的参数信息
        canvas.create_oval(width/2-k,height/2-k,width/2+k,height/2+k,width=1)
        k+=j
        j+=0.5
    mainloop()



if __name__ =="__main__":
    circle(1080,720,'purple')