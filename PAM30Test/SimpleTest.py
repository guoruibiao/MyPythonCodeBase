# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/7'
#    __Desc__ = 模拟IE进行网页的点击。在同一目录下必须包含PAM30这个py文件

from PAM30 import PAMIE

ie = PAMIE()

# for i in range(1,100,1):
#     ie.navigate('http://blog.csdn.net/marksinoberg/article/details/51852241')
#     ie.refresh()
# ie.quit()

ie.navigate('https://github.com/login')
ie.setTextBox('login', 'marksinoberg@gmail.com')
ie.setTextBox('password', 'guoruibiao285514')
ie.clickButton('commit')
