# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/6'
#    __Desc__ = 手动的写一个字典

file = open(r'./directory.txt','wb')
pwdstr = ''
for i in range(000,1000,1):
    pwdstr = pwdstr+str(i)+"\n"
file.write(pwdstr)
file.close()
print  "字典写入完毕！"
