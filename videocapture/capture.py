# coding:utf-8

from VideoCapture import Device
import Device
from time import time
import string

interval = 2
cam = Device(devnum=0,showVideoWindow=0)

cam.save('capture.png',timestamp=3,blodfont=1,quality=75)

i = 0
quant = interval *0.1
starttime = time()
while 1:
    lasttime = now = int((time()-starttime)/interval)
    print i
    cam.saveSnapshot('capture.png',timestamp=3,boldfont=1)
    i=i+1
    while now == lasttime:
        now = ((time()-starttime)/interval)
        time.sleep(quant)