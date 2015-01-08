# coding: utf-8
#socket非异步测试程序
from socket import *

myHost = '127.0.0.1'
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)
while True:
    connection, address = sockobj.accept()
    print 'Server connected by', address
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send('Echo=>' + data)
    connection.close()

