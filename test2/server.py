# 服务端
import random
from socket import *
import time

ACK_0 = '0'
ACK_1 = '1'
NAK = '-1'


def receive(conn, addr):
    while True:
        index = random.sample(range(0, 3), 1)
        try:
            data = conn.recv(BUFSIZ)  # 读取已链接客户的发送的消息
            time.sleep(1)
        except Exception:
            print("断开的客户端", addr)
            break
        receiveStr = data.decode(COD)
        if not receiveStr:
            break
        flag = int(receiveStr[0])
        messege = receiveStr[2:]
        print("接受到客户端的内容:%s,收到的序号为:%d" % (receiveStr, flag))
        if not data:
            break
        # print(index[0])
        if index[0] == 1:
            print("超时了")
            time.sleep(3)
        else:
            conn.send(receiveStr.encode(COD))
            # if flag == 0:
            #     conn.send(ACK_1.encode(COD))  # 0号帧收到，想收1号帧
            # else:
            #     conn.send(ACK_0.encode(COD))  # 1号帧收到，想收0号帧
    conn.close()  # 关闭客户端链接


if __name__ == '__main__':
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
