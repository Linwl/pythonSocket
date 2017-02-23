#!usr/bin/env pyhton
# coding:utf-8

from socket import  *
from time import ctime

#服务器配置信息
HOST ="127.0.0.1"
PORT = 6604
BufSiza = 2048
Addr = (HOST,PORT)

def TcpConnect():
    """
    建立TCP连接
    """
    try:
        tcpSerSock = socket(AF_INET, SOCK_STREAM)
        tcpSerSock.bind(Addr)
        tcpSerSock.listen(5)
        return tcpSerSock
    except Exception,e:
        print e.message


def Send(tcpSerSock):
    try:
        while True:
            print "等待连接中...."
            tcpCliSock, addr = tcpSerSock.accept()
            print '...connected from: ', addr

            while True:
                try:
                    data = tcpCliSock.recv(BufSiza)
                    if not data:
                        break
                    tcpCliSock.send("[%s]%s" % (ctime(), data))
                    tcpCliSock.close()
                except Exception, e:
                    print "服务器接收错误", e.message
                    tcpCliSock.send("无法识别该请求!")
    except EOFError,KeyboardInterrupt:
        tcpSerSock.close()

def main():
    tcpSerSock = TcpConnect()
    Send(tcpSerSock)
    tcpSerSock.close()

if __name__ == '__main__':
    main()


