# coding:utf-8

import Image

image = Image.open('hu.jpg')
# 格外应该注意这里 接受一个元组参数
image.resize((200, 200))
# 链式的调用可以显示改变的效果，换行了貌似就不行了。:-)
image.rotate(45) # 旋转45°
image.transpose(Image.FLIP_LEFT_RIGHT).show() # 左右对换
image.transpose(Image.FLIP_TOP_BOTTOM).show() # 上下对换
image.transpose(Image.ROTATE_90).show()       # 旋转90°
