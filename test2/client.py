# 客户端
from socket import *
from time import ctime

if __name__ == '__main__':
    HOST = '127.0.0.1'  # 服务端ip
    PORT = 21566  # 服务端端口号
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
    tcpCliSock.connect(ADDR)  # 连接服务器
    user_input = ''
    user_input = input()
    tcpCliSock.settimeout(3)
    while user_input != 'quit':
        try:
            tcpCliSock.sendto(user_input.encode('utf-8'), ADDR)
            # tcpCliSock.send(user_input.encode('utf-8'))
            returnData = tcpCliSock.recv(BUFSIZ)  # 读取消息
            print(returnData.decode('utf-8'))
        except timeout:
            print("dfsf")
            # tcpCliSock.close()
            # reConnnectTCP()
        finally:
            user_input = input()
    tcpCliSock.close()  # 关闭客户端
