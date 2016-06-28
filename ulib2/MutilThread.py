# coding:UTF-8

from threading import Thread
from Queue import Queue
from time import sleep

# 预先定义一些变量，虽然我很讨厌这种C预言式的方式
q = Queue()
NUM = 2;
JOBS = 10

def doSomethingUsing(args):
    print args

def working():
    while True:
        args = q.get()
        doSomethingUsing(args)
        sleep(1)
        q.task_done()

for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)
    t.start()

for i in range(JOBS):
    q.put(i)

q.join()

