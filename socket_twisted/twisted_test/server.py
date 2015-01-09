# coding: utf-8

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

# 定义你Protocol类
class SimpleLogger(Protocol):
    #当你得到一个连接时，事件处理器 connectionMade被调用
    def connectionMade(self):
        print 'Got connection from', self.transport.client         #它也有一个client属性，其中包含了客户端的地址(主机名和端口)
    #当你丢失了一个连接时，connectionLost被调用
    def connectionLost(self, reason):
        print self.transport.client, 'disconnected'
    #从客户端接受数据使用处理器 dataReceived
    def dataReceived(self, data):
        print data
        self.transport.write("recv...%s" % data)

# 实例化Factory
factory = Factory()
# 设置factory的protocol属性以便它知道使用哪个protocol与客户端通信(这就是所谓的你的自定义
# protocol)
factory.protocol = SimpleLogger
# 监听指定的端口
reactor.listenTCP(1234, factory)
# 开始运行主程序
reactor.run()