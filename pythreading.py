#!/usr/bin/python

import threading,time,datetime

class Print(threading.Thread):
    def __init__(self, delay):
        threading.Thread.__init__(self)
        self.delay = delay
        print ('init '+self.getName())

    def run(self):
        global a
        threadLock.acquire()
        for i in a:
            print (self.getName()+':'+str(i))
            #print (datetime.datetime.now())
            time.sleep(self.delay)
        threadLock.release()
        print ('exit '+self.getName())

class Set(threading.Thread):
    def __init__(self, delay):
        threading.Thread.__init__(self)
        self.delay = delay
        print ('init '+self.getName())

    def run(self):
        global a
        count = 1
        threadLock.acquire()
        while(count<=len(a)):
            a[-count] = 1
            count += 1
            print (self.getName()+':',a)
            time.sleep(self.delay)
        threadLock.release()
        print ('exit '+self.getName())

threadLock = threading.Lock()

if __name__ == '__main__':
    a = [0,0,0,0,0]
    t1 = Print(1)

    t2 = Set(1)
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    print ("end")



