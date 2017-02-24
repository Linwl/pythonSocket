#!usr/bin/env python
# coding:utf - 8
'''
TCPServer 服务器端
'''

import SocketServer
from SocketServer import StreamRequestHandler as SRH
from time import ctime

HOST = "127.0.0.1"
PORT = 6604
ADDR = (HOST,PORT)


class Servers(SRH):
    def handle(self):
        print 'got connection from ', self.client_address
        self.wfile.write('connection %s:%s at %s succeed!' % (HOST, PORT, ctime()))
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print data
            print "RECV from ", self.client_address[0]
            self.request.send(data)


print '等待连接....'
server = SocketServer.ThreadingTCPServer(ADDR, Servers)
server.serve_forever()


