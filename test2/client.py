# 客户端
from socket import *
from time import ctime

Flag = 0
reSendFlag = False
if __name__ == '__main__':
    HOST = '127.0.0.1'  # 服务端ip
    PORT = 21566  # 服务端端口号
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
    tcpCliSock.connect(ADDR)  # 连接服务器
    user_input = ''
    user_input = input().strip()
    tcpCliSock.settimeout(0.3)
    while user_input != 'quit':
        if reSendFlag==0:
            user_input = str(Flag) + ':' + user_input
        reSendFlag = False
        try:
            tcpCliSock.sendto(user_input.encode('utf-8'), ADDR)
            # tcpCliSock.send(user_input.encode('utf-8'))
            returnData = tcpCliSock.recv(BUFSIZ)  # 读取消息
            returnData = int(returnData.decode('utf-8'))
            if returnData == -1:
                print("发送了错误帧")
                reSendFlag = True
            else:
                print("信息已经收到，返回确认帧为ACK(%d)" % returnData)
                Flag = returnData
        except timeout:
            print("发生了超时")
            reSendFlag=True
        finally:
            if reSendFlag != 1:
                user_input = input().strip()
    tcpCliSock.close()  # 关闭客户端
