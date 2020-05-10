# 客户端
import json
import pickle
from socket import *

# RIP = {"N2": (4, 'C'), "N3": (8, 'C'), "N6": (4, 'C'), "N8": (3, 'C'), "N9": (5, 'C')}
from test3.RIP import RIP

RIPList = []


def init():
    r1 = RIP('N2', 4, 'C')
    r2 = RIP('N3', 8, 'C')
    r3 = RIP('N6', 4, 'C')
    r4 = RIP('N8', 3, 'C')
    r5 = RIP('N9', 5, 'C')
    RIPList.append(r1)
    RIPList.append(r2)
    RIPList.append(r3)
    RIPList.append(r4)
    RIPList.append(r5)


if __name__ == '__main__':
    init()
    HOST = '127.0.0.1'  # 服务端ip
    PORT = 21566  # 服务端端口号
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
    tcpCliSock.connect(ADDR)  # 连接服务器
    while True:
        data_string = pickle.dumps(RIPList)
        tcpCliSock.send(data_string)  # 发送消息
        try:
            data = tcpCliSock.recv(BUFSIZ)  # 读取消息
            print("服务端返回内容：", data.decode('utf-8'))
            break
        except timeout:
            print("超时")
        if not data:
            break
    tcpCliSock.close()  # 关闭客户端
