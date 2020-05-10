# 服务端
import ast
import pickle
from socket import *
import time
import json

B_table = {'N1': (7, 'A'), 'N2': (2, 'C'), 'N6': (8, 'F'), 'N8': (4, 'F')}


def receive(conn, addr):
    while True:
        try:
            data = conn.recv(BUFSIZ)  # 读取已链接客户的发送的消息
            string = pickle.loads(data)
            print(string)
        except Exception:
            print("断开的客户端", addr)
            break
        receiveStr = "OK"  # 变大写
        conn.send(receiveStr.encode(COD))  # 发送消息给已链接客户端
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
