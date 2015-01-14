# coding=utf-8
import json
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
import datetime
import multiprocessing
import time
multiprocessing.freeze_support()


class Greeter(Protocol):
    def send_message(self, msg):
        self.transport.write("%s" % msg)
        print msg

    def dataReceived(self, data):
        data = data.replace('/**end**/', '')
        print 'response'
        print json.loads(data)
        # print datetime.datetime.now()-now
        self.transport.loseConnection()
        reactor.stop()



def gotProtocol(p):
    #data = {"commodity_id": "BAG","trader_id": "999000010","quantity": "10","price": "100","order_ip": "192.8.8.1","traderID": "999000010","amount": "1000"}
    print 'request'
    # p.sendMessage('[{"action":"frozen_funds", "data":{"trader_id":"999000010", "amount":100}}]')
    # p.sendMessage('[{"action":"view_all_commodity"}]')
    #p.send_message('[{"action":"put_buy_order","data":{"commodity_id": "BAG","trader_id": "999000010","quantity": "10","price": "100","order_ip": "192.8.8.1","traderID": "999000010","amount": "1000"}}]')
    p.send_message('[{"action":"view_salable_commodity", "data":{"trader_id":"999000010"}}]')
    #p.send_message('[{"action":"put_buy_order","data":{"commodity_id": "BAG","trader_id": "999000010","quantity": "99","price": "99.0","order_ip": "123.123.123.123","buy_type":"GTD","need_invoice":"True","order_no":"107","receiver_no":"100","invoice_no":"5"}}]')
    #p.send_message('[{"action":"view_trader_stock", "data":{"trader_id":"999000010", "commodity_id":"BAG"}}]')
    # p.sendMessage('[{"action":"view_salable_commodity", "data":{"trader_id":"999000010"}}, {"action":"view_trader_stoc
    # k", "data":{"trader_id":"999000010", "commodity_id":"BAG"}}]')
    # print datetime.datetime.now()-now

def getError(p):
    print p


# server_ip = 'localhost'
# point = TCP4ClientEndpoint(reactor, server_ip, 10001)
# d = connectProtocol(point, Greeter())
# d.addCallback(gotProtocol)
# d.addErrback(getError)
# now = datetime.datetime.now()
# reactor.run()

def func(msg):
    print msg
    server_ip = 'localhost'
    point = TCP4ClientEndpoint(reactor, server_ip, 10001)
    d = connectProtocol(point, Greeter())
    d.addCallback(gotProtocol)
    d.addErrback(getError)
    now = datetime.datetime.now()
    reactor.run()
    # for i in xrange(2):
    #     print msg
    #     time.sleep(1)
    return "done " + msg

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=10)
    result = []
    for i in xrange(10):
        msg = "%d" %(i)
        result.append(pool.apply_async(func, (msg, )))
        #pool.apply_async(func)
    pool.close()
    pool.join()
    for res in result:
        print res.get()
    print "Sub-process(es) done."
