# coding:utf-8

import Image

image = Image.open("hu.jpg")

# 下面的几行代码可以较好的呈现出图片的变化情况
image.rotate(45).show()
image.rotate(90).show()
image.rotate(180).show()
image.rotate(270).show()
image.rotate(360).show()
