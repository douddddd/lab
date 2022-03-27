#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: William

import socket, time, threading

# recv_data = ""
# 发送
# def main():
#     # 1、创建一个UDP套接字
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#     # 2. 准备接收方的地址和端口，'192.168.0.107'表示目的ip地址，8080表示目的端口号  (需要修改)
#     dest_addr = ('127.0.0.1', 12344)  # 注意这是一个元组，其中ip地址是字符串，端口号是数字
#     print(recv_data)
#     # 3. 发送数据到指定的ip和端口
#     while True:
#         udp_socket.sendto(recv_data.encode('utf-8'), dest_addr)
#         time.sleep(1)
#
#     # 4. 关闭套接字
#     udp_socket.close()


# 接收
def main2():
    # 1、创建一个UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socketSend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地的相关信息，如果不绑定，则系统会随机分配一个端口号
    # local_addr为本地IP和端口
    local_addr = ('192.168.137.232', 12341)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    udp_socket.bind(local_addr)
    # dest_addr 为目的IP和端口
    dest_addr = ('192.168.137.92', 12341)  # 注意这是一个元组，其中ip地址是字符串，端口号是数字
    # 3. 等待接收对方发送的数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数

    while len(recv_data) != 0:
        # 4、打印接收到的数据
        time.sleep(20)
        print(recv_data)
        # 3. 发送数据到指定的ip和端口
        udp_socketSend.sendto(recv_data[0], dest_addr)




    # 5. 关闭套接字
    udp_socket.close()
    udp_socketSend.close()


if __name__ == '__main__':
    main2()
    # main()
