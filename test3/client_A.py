# 客户端
import copy
import operator
import pickle
from filecmp import cmp
from socket import *

# RIP = {"N2": (4, 'C'), "N3": (8, 'C'), "N6": (4, 'C'), "N8": (3, 'C'), "N9": (5, 'C')}
from test3.RIP import RIP

A_table = []


def cmp(oldlist, newlist):
    if len(oldlist) != len(newlist):
        return False
    else:
        for i in range(len(oldlist)):
            if not oldlist[i].cmp(newlist[i]):
                return False
    return True


def init():
    r1 = RIP('N1', 2, 'B')
    A_table.append(r1)


if __name__ == '__main__':
    init()
    HOST = '127.0.0.1'  # 服务端ip
    PORT = 21566  # 服务端端口号
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
    tcpCliSock.connect(ADDR)  # 连接服务器
    tcpCliSock.settimeout(0.1)
    flag = False
    while True:
        RIP.changenext(A_table, 'A')
        data_string = pickle.dumps(A_table)
        tcpCliSock.send(data_string)  # 发送消息
        try:
            data = tcpCliSock.recv(BUFSIZ)  # 读取消息
            break
        except timeout:
            tcpCliSock.settimeout(0.3)
            A_table[0].distance = 16
            print("3分钟还没有收到相邻路由器的更新路由表")
    tcpCliSock.close()  # 关闭客户端
