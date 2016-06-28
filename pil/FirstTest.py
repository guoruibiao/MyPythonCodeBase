# coding:utf-8
import Image

"""
format: 识别图像的源格式，如果不是从文件中读取的，则被设置为None值
size:   返回的一个元组，有两个元素，其值为像素意义上的宽和高
mode:   RGB，此外还有L（Luminance),CTMK(pre-press image,呵呵我也不知道这是个神马）
"""

image = Image.open('hu.jpg')
print image.format, image.size, image.mode
# 用于将图片 使用本地的图片查看器打开
image.show()
