# 服务端
from socket import *
import time


def receive(conn, addr):
    while True:
        try:
            data = conn.recv(BUFSIZ)  # 读取已链接客户的发送的消息
        except Exception:
            print("断开的客户端", addr)
            break
        receiveStr = data.decode(COD)
        print("客户端发送的内容:", receiveStr)
        if not data:
            break
        receiveStr = receiveStr.upper()  # 变大写
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
