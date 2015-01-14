import threading
from time import time
from twisted.internet import reactor
from twisted.internet.threads import deferToThread

__author__ = 'Administrator'

import urllib2
MAX = 100
count = MAX


def func(i, web_site):

    url = "http://www.baidu.com"

    req = urllib2.Request(url)

    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print i, web_site, time() - mt

# def cb(a, web_site, i):
#     global count
#     count -= 1
#     print MAX - count, i, web_site, time() - mt
#     if count == 0:
#         reactor.stop()


mt = time()
print '----- current time ', mt, '--------'

if __name__ == '__main__':

    web_sites = ['http://www.baidu.com', 'http://www.sohu.com', 'http://www.sina.com',
             'http://www.163.com', 'http://www.qq.com', 'http://www.taobao.com',
             'http://www.jd.com', 'http://mail.126.com', 'http://www.bing.com']

    for i in range(count):
        print i, time()-mt
        web_site = web_sites[i % 9]
        t = threading.Thread(target=func, args=(i, web_site, ))
        t.start()
        # d = deferToThread(func, web_site)
        # d.addCallback(cb, web_site, i)
    print '======', time()-mt

    # reactor.run()