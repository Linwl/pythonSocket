#!usr/bin/env pyhton
# coding:utf-8

from socket import  *

#客户端配置信息
HOST ='127.0.0.1'
PORT = 6604
BufSiza = 2048
Addr = (HOST,PORT)


def TcpConnect():
    '''
    连接服务器
    :return:
    '''
    try:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(Addr)
        return tcpCliSock
    except Exception,e:
        print e.message

def Send(tcpCliSock):
    while True:
        data = raw_input(">")
        if not data:
            break
        try:
            tcpCliSock.send(data)
            data = tcpCliSock.recv(BufSiza)
            if not data:
                break
            print data
        except Exception,e:
            print "客户端错误",e.message

def main():
    tcpCliSock=TcpConnect()
    Send(tcpCliSock)
    tcpCliSock.close()

if __name__ == '__main__':
    main()