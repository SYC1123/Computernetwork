# 服务端
import random
from socket import *
import time

ACK_0 = '0'
ACK_1 = '1'
NAK = '-1'
TIMEOUT_1 = '2'  # 确认帧未及时返回
TIMEOUT_2 = '3'  # 数据帧丢失


def receive(conn, addr):
    NowFlag = -1
    BeforeFlag = -1
    ReceiveMessageList = []
    CanAddFlag = True  # 一次发送多次重复帧能否添加
    while True:
        index = random.sample(range(0, 4), 1)
        try:
            data = conn.recv(BUFSIZ)  # 读取已链接客户的发送的消息
            time.sleep(0.1)
        except Exception:
            print("断开的客户端", addr)
            break
        receiveStr = data.decode(COD)
        if not receiveStr:
            break
        NowFlag = int(receiveStr[0])
        messege = receiveStr[2:]
        if index[0] == 0:  # 确认帧未及时返回
            print("（ReceivedMessage:%s,Order:%d）,确认帧未及时返回" % (messege, NowFlag))
            BeforeFlag = NowFlag
            if CanAddFlag:
                ReceiveMessageList.append(messege)
                CanAddFlag = False
            time.sleep(0.2000001)
        elif index[0] == 1:  # 数据帧丢失
            print("数据帧丢失")
            time.sleep(0.2000001)
        elif index[0] == 2:
            print("接收到错误帧")
            conn.send(NAK.encode(COD))  # 错误
        else:  # 正确接收
            CanAddFlag = True
            if BeforeFlag == NowFlag:
                print("（ReceivedMessage:%s,Order:%d）,重复帧" % (messege, NowFlag))
            else:
                BeforeFlag = NowFlag
                ReceiveMessageList.append(messege)
                print("（ReceivedMessage:%s,Order:%d）,正确接收" % (messege, NowFlag))
            if len(ReceiveMessageList) != 0:
                for value in ReceiveMessageList:
                    print(value, end=" ")
                print()
            if NowFlag == 0:
                conn.send(ACK_1.encode(COD))  # 0号帧收到，想收1号帧
            else:
                conn.send(ACK_0.encode(COD))  # 1号帧收到，想收0号帧
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
        # if len(ReceiveMessageList)!=0:
        #     for value in ReceiveMessageList:
        #         print(value,end="")
        #     print()
        print("服务器启动，监听客户端链接")
        conn, addr = tcpS.accept()
        print("链接的客户端", addr)
        receive(conn, addr)
    tcpS.closel()
