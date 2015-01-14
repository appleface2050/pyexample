# coding: utf-8
'''
deferred主要做的事情就是将一些可能会耗时，会阻塞主线程的事放到另一个线程中去做，然后返回一个deferred对象给主线程，
主线程给这个deferred注册一些回调函数，当在子线程中耗时的函数处理完后会调用deferred的callback函数，调用之前注册好的回调函数，
一次实现异步操作。
'''

import time
def largeFibonnaciNumber(data_list):
    """
    耗时的事
    """
    for i in data_list:
        print i

    TARGET = 10000

    first = 0
    second = 1
    
    for i in xrange(TARGET - 1):
        new = first + second
        first = second
        second = new
    time.sleep(3)
    return second

from twisted.internet import threads, reactor

def fibonacciCallback(result):
    """
    回调函数
    打印耗时函数的返回结果
    """
    print "largeFibonnaciNumber result =", result

def run():
    """
    主函数
    """
    # 将耗时函数放入另一个线程执行，返回一个deferred对象
    d = threads.deferToThread(largeFibonnaciNumber,(1,2,3,4))
    # 添加回调函数
    d.addCallback(fibonacciCallback)
    print "1st line after the addition of the callback"
    print "2nd line after the addition of the callback"

if __name__ == '__main__':
    run()
    reactor.run()
