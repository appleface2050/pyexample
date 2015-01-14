import time
from twisted.internet import reactor
from twisted.internet.defer import DeferredList
from twisted.web.client import getPage

__author__ = 'Administrator'


now = time.time()
MAX = 100
count = MAX

web_sites = ['http://www.baidu.com', 'http://www.sohu.com', 'http://www.bing.com',
             'http://www.163.com', 'http://www.qq.com', 'http://www.taobao.com',
             'http://www.jd.com', 'http://mail.126.com', 'http://www.amazon.com']

def func(a, web_site, i):
    global count
    count -= 1
    print MAX - count, i, web_site, time.time() - now
    if count == 0:
        reactor.stop()

if __name__ == '__main__':
    main_now = time.time()
    print '--------', main_now - now
    for i in xrange(count):
        print i, time.time() - main_now
        web_site = 'http://www.baidu.com'
        web_site = web_sites[i % 9]
        d = getPage(web_site)
    # DeferredList(dl).addCallback(func)
        d.addCallback(func, web_site, i)
    print '-------', time.time() - main_now
    reactor.run()

