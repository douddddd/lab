import cv2
from datetime import datetime
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
out = cv2.VideoWriter('/home/pi/communication_py/video/'+str(time.time())+'.mp4',fourcc ,fps, size)

# 确定视频打开并循环读取
i=0
while(cap.isOpened()):
    i=i+1
    print(i)
    # 逐帧读取，ret返回布尔值
    # 参数ret为True 或者False,代表有没有读取到图片
    # frame表示截取到一帧的图片
    ret, frame = cap.read()
    if ret == True:
        # 垂直翻转矩阵
        # frame = cv2.flip(frame,0)
        print(type(frame))
        print(frame.shape)
        out.write(frame)

    else:
        break

# 释放资源
cap.release()
out.release()
# 关闭窗口