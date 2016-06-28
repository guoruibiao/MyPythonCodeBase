# coding:utf-8

import Image
import glob, os

size = 128, 128

image = Image.open('hu.jpg')
# 调用thumbnail方法完成对图片的处理
image.thumbnail(size, Image.ANTIALIAS)
image.save("hu_scale.jpg")
