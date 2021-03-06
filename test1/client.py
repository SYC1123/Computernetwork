# 客户端
from socket import *
from time import ctime

HOST = '127.0.0.1'  # 服务端ip
PORT = 21566  # 服务端端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
tcpCliSock.connect(ADDR)  # 连接服务器
while True:
    data = input('>>',).strip()
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))  # 发送消息
    try:
        data = tcpCliSock.recv(BUFSIZ)  # 读取消息
        print("服务端返回内容：", data.decode('utf-8'))
    except timeout:
        print("超时")
        # tcpCliSock.send(data.encode('utf-8'))  # 发送消息
    if not data:
        break
    # print("服务端返回内容：", data.decode('utf-8'))
tcpCliSock.close()  # 关闭客户端
