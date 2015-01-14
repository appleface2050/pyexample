# coding: utf-8
'''
multiprocessing演示，
processes数值为启动的进程数量，也就是一次性处理func的数量
'''

import multiprocessing
import time
multiprocessing.freeze_support()

def func(msg):
    for i in xrange(2):
	    print msg
	    time.sleep(1)
    return "done " + msg
 
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(10):
        msg = "hello %d" %(i)
        result.append(pool.apply_async(func, (msg, )))
    pool.close()
    pool.join()
    for res in result:
        print res.get()
    print "Sub-process(es) done."