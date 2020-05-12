# 客户端
import copy
import operator
import pickle
from filecmp import cmp
from socket import *

# RIP = {"N2": (4, 'C'), "N3": (8, 'C'), "N6": (4, 'C'), "N8": (3, 'C'), "N9": (5, 'C')}
from test3.RIP import RIP

C_table = []


def cmp(oldlist, newlist):
    if len(oldlist)!=len(newlist):
        return False
    else:
        for i in range(len(oldlist)):
            if not oldlist[i].cmp(newlist[i]):
                return False
    return True

def init():
    r1 = RIP('N2', 4, 'A')
    r2 = RIP('N3', 8, 'Z')
    r3 = RIP('N6', 4, 'F')
    r4 = RIP('N8', 3, 'D')
    r5 = RIP('N9', 5, 'E')
    C_table.append(r1)
    C_table.append(r2)
    C_table.append(r3)
    C_table.append(r4)
    C_table.append(r5)


if __name__ == '__main__':
    init()
    HOST = '127.0.0.1'  # 服务端ip
    PORT = 21566  # 服务端端口号
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
    tcpCliSock.connect(ADDR)  # 连接服务器
    tcpCliSock.settimeout(0.3)
    while True:
        copylist = copy.deepcopy(C_table)
        RIP.addvalue(copylist)
        RIP.changenext(copylist, 'C')
        data_string = pickle.dumps(copylist)
        tcpCliSock.send(data_string)  # 发送消息
        try:
            data = tcpCliSock.recv(BUFSIZ)  # 读取消息
            # print("服务端返回内容：", data.decode('utf-8'))
            getList = pickle.loads(data)
            print('收到的RIP报文')
            print('---------------------------------')
            for item in getList:
                item.output(0)
            print('---------------------------------')
            oldlist = copy.deepcopy(C_table)
            RIP.updatetable(C_table, getList)
            if cmp(oldlist,C_table):
                print("路由表稳定")
                break
            else:
                print("更新后的路由表")
                print('---------------------------------')
                for item in C_table:
                    item.output(1)
                print('---------------------------------')
            # break
        except timeout:
            print("超时")
    tcpCliSock.close()  # 关闭客户端
