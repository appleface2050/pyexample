# coding: utf-8

#socket非异步测试程序


import sys
from socket import *
serverHost = '127.0.0.1'
serverPort = 50007

message = ['Hello network world']
if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = sys.argv[2:]

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))
for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    print 'Client received:', repr(data)
sockobj.close()