# coding: utf-8

#socket非异步测试程序


import sys
from socket import *
# serverHost = '127.0.0.1'
serverHost= '192.168.182.129'
serverPort = 1234

message = ['qqqqqq']
#message.append("end")
print sys.argv
# if len(sys.argv) > 1:
#     serverHost = sys.argv[1]
#     if len(sys.argv) > 2:
#         message = sys.argv[2:]

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))
for line in message:
    sockobj.send("qqqq\n")
    data = sockobj.recv(1011)
    print 'Client received:',data
sockobj.close()