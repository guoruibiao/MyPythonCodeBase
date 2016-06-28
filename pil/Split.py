#coding:utf-8

import Image

"""
    r,g,b=im.split()#分割成三个通道，此时r,g,b分别为三个图像对象。
    im=Image.merge("RGB",(b,g,r))#将b,r两个通道进行翻转。
"""

image = Image.open('hu.jpg')
r,g,b = image.split()
r.save('Split/r.jpg','jpeg')
g.save('Split/g.jpg','jpeg')
b.save('Split/b.jpg','jpeg')
image = Image.merge("RGB",(b,g,r))
image.save('Split/mergedByBGR.jpg','jpeg')
image = Image.merge("RGB",(g,r,b))
image.save('Split/mergedByGRB.jpg','jpeg')
image = Image.merge("RGB",(r,g,b))
image.save('Split/mergedByRGB.jpg','jpeg')
