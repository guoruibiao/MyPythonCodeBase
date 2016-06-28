#coding:utf-8

import Image

"""
    r,g,b=im.split()#分割成三个通道，此时r,g,b分别为三个图像对象。
"""

image = Image.open('hu.jpg')
r,g,b = image.split()
r.save('Split/r.jpg','jpeg')
g.save('Split/g.jpg','jpeg')
b.save('Split/b.jpg','jpeg')

