import cv2 
from datetime import datetime
import socket, time, threading
import numpy as np
import os
import time
# VideoCapture方法是cv2库提供的读取视频方法
cap = cv2.VideoCapture('/home/pi/communication_py/test.mp4')
# 设置需要保存视频的格式“xvid”
# 该参数是MPEG-4编码类型，文件名后缀为.avi
fourcc = cv2.VideoWriter_fourcc(*'mp4v')#mp4
#fourcc = cv2.VideoWriter_fourcc(*'XVID')avi
# 设置视频帧频
fps = cap.get(cv2.CAP_PROP_FPS)
# 设置视频大小
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# VideoWriter方法是cv2库提供的保存视频方法
# 按照设置的格式来out输出

print(fps)
print(size)
tcp_client_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# 目的信息    服务器IP
server_ip = "192.168.137.92"
server_port = 12341
tcp_client_socket.connect((server_ip, server_port))


def changeImage(img, pra):
    #pra为缩放的倍率
    height, width = img.shape[:2]
    #此处要做integer强转,因为.resize接收的参数为形成新图像的长宽像素点个数
    size = (int(height*pra), int(width*pra))
    img_new = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    return img_new


# 确定视频打开并循环读取
i=0
while 1:
    while(cap.isOpened()):
        i=i+1
        print(i)
        if i==3000:    
            print(i)
            i=0
            break
        # 参数ret为True 或者False,代表有没有读取到图片
        # frame表示截取到一帧的图片
        ret, frame = cap.read()
        
        if ret == True:
            # 垂直翻转矩阵
            # frame=changeImage(frame, 0.1)
            # print(type(frame))
            # print(frame.shape)
            # img_encode = cv2.imencode('.jpg',frame)[1]
            # data_encode = np.array(img_encode)
            # data = data_encode.tostring()
            # clisocket.sendto(data, ('192.168.137.92', 12341))
            tcp_client_socket.send( frame.tobytes() )
            print('success')
            recv_data = tcp_client_socket.recv(1024)
            print(recv_data)
        else:
            break
    time.sleep(150)
tcp_client_socket.close()
print('Video Reading & TCP Sending Stopped!')

# 释放资源
# 关闭窗口