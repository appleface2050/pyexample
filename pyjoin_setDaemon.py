#! /usr/bin/env python
 
import threading
import time
 
class myThread(threading.Thread):
  def __init__(self, threadname):
    threading.Thread.__init__(self, name=threadname)
    self.st = 2 
 
  def run(self):
    time.sleep(self.st)
    print (self.getName())

  def setSt(self, t): 
    self.st = t 
 
def fun1():
  t1.start()
  print ("fun1 start")
 
def fun2():
  t2.start()
  print ("fun2 start")
 
t1=myThread("t1")
t2=myThread("t2")
t2.setSt(5);
#t2.setDaemon(True)

fun1()
fun2()
#t2.join()
print ("end")
