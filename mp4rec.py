# import socket, time, threading
# import cv2
# import numpy as np
# svrsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# svrsocket.bind(('192.168.137.92', 12341))
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')#mp4
# #fourcc = cv2.VideoWriter_fourcc(*'XVID')avi
# # 设置视频帧频
# fps = 30
# # 设置视频大小
# size = (160,120)
# out = cv2.VideoWriter('/home/pi/communication_py/video/'+str(time.time())+'.mp4',fourcc ,fps, size)
# i=0
# while 1:
    
#     data = svrsocket.recvfrom(10000)
#     print(data)
#     npdata=np.array(data)
#     print(npdata.shape)
#     out.write(npdata)


# # 5. 关闭套接字
# udp_socket.close()
# udp_socketSend.close()
# out.release()
import socket
import time
import cv2
import numpy as np
import os
# 创建socket
tcp_server_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# 本地信息  本机IP
address = ('192.168.137.92', 12341)
# 绑定
tcp_server_socket.bind(address)
# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
# listen里的数字表征同一时刻能连接客户端的程度.
tcp_server_socket.listen(128)
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
# clientAddr 是元组（ip，端口）
client_socket, clientAddr = tcp_server_socket.accept()
cap = cv2.VideoCapture('/home/pi/test.mp4')
# 设置视频帧频
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
# 设置视频大小
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)
recv_data_whole = bytes()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')#mp4
# VideoWriter方法是cv2库提供的保存视频方法
# 按照设置的格式来out输出
out = cv2.VideoWriter('/home/pi/communication_py/video/'+str(time.time())+'.mp4',fourcc ,fps, size)
numbers=0
while 1:
    # 接收对方发送过来的数据，和udp不同返回的只有数据
    recv_data = client_socket.recv(3000000)  # 接收n个字节
    if numbers==3000:
        numbers=0
    if len(recv_data) == 0 :
        # 关闭socket
        
        client_socket.close()
        tcp_server_socket.close()
        print('客户端已断开连接,服务结束')
        break
        # client_socket, clientAddr = tcp_server_socket.accept() # 也可以等待重连
    else:
        recv_data_whole += recv_data
        # print('接收到的数据长度为:', recv_data_whole.__len__())

        if recv_data_whole.__len__() == 2764800 : # 720p RGB单张图像大小
            # 字节数据转回图片
            frame = np.frombuffer(recv_data_whole, dtype=np.uint8).reshape([720,1280,3]) 
            cv2.imwrite(os.path.join('/home/pi/communication_py/video/'+str(numbers)+'.jpg'), frame)
            numbers=numbers+1
            # frame = cv2.flip(frame,0)
            # frame.save(str(time.time())+'dog.jpg')
            recv_data_whole = bytes()
            # print('succ')
            print(frame.shape)
            print(type(frame))
            out.write(frame)
            
            client_socket.send("image has been received!".encode('gbk'))
            # 回传信息，很重要，具有同步功能
            # client_socket.send("image has been received!".encode('gbk'))
out.release()