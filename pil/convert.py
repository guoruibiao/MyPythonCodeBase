# coding:utf-8

import Image, ImageFilter

"""
色彩空间的变换，convert函数可以用来将图像转换为不同的色彩模式
"""

image = Image.open('hu.jpg')
# image.filter(ImageFilter.DETAIL).show() # 真实效果展现
# image.filter(ImageFilter.BLUR).show()   # 以模糊化的效果展现
# image.filter(ImageFilter.CONTOUR).show()  # 以铅笔画的效果展现
# image.filter(ImageFilter.FIND_EDGES).show()  # 以铅笔画黑色背景展示
# image.filter(ImageFilter.EDGE_ENHANCE).show()  # 线条高亮的显示效果
# image.filter(ImageFilter.EDGE_ENHANCE_MORE).show()  # 强化线条高亮
# image.filter(ImageFilter.EMBOSS).show()  # 浮雕效果
# image.filter(ImageFilter.GaussianBlur).show()  # 也是模糊化的显示效果
# image.filter(ImageFilter.SMOOTH_MORE).show()
# image.filter(ImageFilter.GaussianBlur).save('Filter/GaussianBlur.jpg','jpeg')
image.transpose(Image.FLIP_LEFT_RIGHT).save('left_to_right.jpg','jpeg')