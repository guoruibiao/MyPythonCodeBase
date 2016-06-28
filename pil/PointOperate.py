# coding:utf-8

import Image

"""
    image.point(function) 这个function接收一个参数，且对图像的每一个点都会进行这个函数的变换
"""

image = Image.open('hu.jpg')
image = image.point(lambda i : i * 1.5)
image.show()