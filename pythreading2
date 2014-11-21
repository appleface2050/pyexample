#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

class MyThread(threading.Thread):
    # def __init__(self):
    #     # threading.Thread.__init__(self)
    #     # print self.name," init"

    def run(self):
        #global num
        global text
        time.sleep(1)
        text = self.name
        print text
        self.name
        #num += 1
        #msg = self.name+'set num to '+str(num)
        #print msg

class MyThread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print self.name," init"
        self.mutex = threading.Lock()

    def run(self):
        #global num
        global text
        time.sleep(1)

        self.mutex.acquire()
        #num+=1
        #msg = self.name+'set num to '+str(num)
        #print msg
        text = self.name
        print text
        print self.name
        self.mutex.release()

text = ""
num = 0

def test():
    for i in range(5):
        t = MyThread()
        t.start()

def test2():
    for i in range(5):
        t = MyThread2()
        t.start()


if __name__ == '__main__':
    test()
    test2()
