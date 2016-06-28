# coding:utf8

import os
import StringIO
import Image,ImageFont,ImageDraw
import pygame

pygame.init()
text = u'This is the text for test'

im = Image.new('RGB',(300,50),(255,255,255))

# os.path.join("fonts","simsun.ttc"),
# font = pygame.font.Font('fonts',14)

# rtext = font.render(text,True,(0,0,0),(255,255,255))

sio = StringIO.StringIO()

pygame.image.save(text,sio)
sio.seek(0)

line = Image.open(sio)
im.paste(line,(10,5))

im.show()
im.save('CreatedTextImage.png')