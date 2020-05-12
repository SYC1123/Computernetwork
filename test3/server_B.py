# 服务端
import ast
import copy
import pickle
from socket import *
import time
import json
from test3.RIP import RIP
from test3.client_C import cmp

B_table = []


# Goal_table = ['N1', 'N2', 'N6', 'N8', 'N9']


def init():
    r1 = RIP('N1', 7, 'A')
    r2 = RIP('N2', 2, 'C')
    r3 = RIP('N6', 8, 'F')
    r4 = RIP('N8', 4, 'E')
    r5 = RIP('N9', 4, 'F')
    B_table.append(r1)
    B_table.append(r2)
    B_table.append(r3)
    B_table.append(r4)
    B_table.append(r5)


def receive(conn, addr):
    while True:
        try:
            time.sleep(0.2)
            data = conn.recv(BUFSIZ)  # 读取已链接客户的发送的消息
            getList = pickle.loads(data)
            print('收到的RIP报文')
            print('---------------------------------')
            for item in getList:
                item.output(0)
            if len(getList) == 1:
                B_table = copy.deepcopy(getList)
                B_table[0].output(0)
            oldlist = copy.deepcopy(B_table)
            RIP.updatetable(B_table, getList)
            if cmp(oldlist, B_table):
                print('---------------------------------')
                print("路由表稳定")
                # break
            else:
                print('更新后的路由表')
                print('---------------------------------')
                for item in B_table:
                    item.output(1)
                print('---------------------------------')
        except Exception:
            print("断开的客户端", addr)
            break
        copylist = copy.deepcopy(B_table)
        RIP.addvalue(copylist)
        RIP.changenext(copylist, 'B')
        receiveStr = pickle.dumps(copylist)
        conn.send(receiveStr)  # 发送消息给已链接客户端
    conn.close()  # 关闭客户端链接


if __name__ == '__main__':
    init()
    COD = 'utf-8'
    HOST = ''  # 主机ip
    PORT = 21566  # 软件端口号
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    SIZE = 10
    tcpS = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
    tcpS.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 加入socket配置，重用ip和端口
    tcpS.bind(ADDR)  # 绑定ip端口号
    tcpS.listen(SIZE)  # 设置最大链接数
    while True:
        print("服务器启动，监听客户端链接")
        conn, addr = tcpS.accept()
        print("链接的客户端", addr)
        receive(conn, addr)
    tcpS.closel()
