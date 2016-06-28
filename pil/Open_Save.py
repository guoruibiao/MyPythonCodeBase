# coding:utf-8
import Image

"""
crop:   从原图层上剪切下来一个给定的矩形大小，此函数接收一个四元素的元组作为其参数，分别代表左上右下，原点为左上角
paste:  粘贴的含义，将剪切到的图像粘贴到某一个位置
merge:  合并，图像的合并操作
"""

image = Image.open('hu.jpg')
box = (100, 100, 300, 300)
mycrop = image.crop(box)
# # mycrop.show()
# mycrop.save('hu_crop.jpg')
#
# # 旋转180° 的图像显示
# # mycrop.transpose(Image.ROTATE_180).show()
#
# # 将剪切板上的图像粘贴到某张图片上，粘贴的位置根据box而定
# image.paste(mycrop, box)
# image.show()
mycrop.rotate(Image.ROTATE_180)
image.paste(mycrop,box)
image.save('pasted.jpg','jpeg')