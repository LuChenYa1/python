import cv2

"""
 在使用OpenCv处理视频时，无论是视频文件还是摄像头画面，都要使用VideoCapture类来进行每一帧图像的处理。
 当传递摄像机编号时，OpenCv则打开相机，实时读取相机画面。
"""
# 打开摄像机
cam = cv2.VideoCapture(0)

"""
直接调用VideoCapture类的read方法，read方法会返回两个参数，一个为是否成功标志，一个为帧画面。
"""
# 获取帧画面
ret, frame = cam.read()
# 循环读取，确保读取成功
while not ret:
	ret, frame = cam.read()

"""
OpenCv底层基于ffmpeg读取视频，
在OpenCv读取视频流时，会设置缓存区，将视频流读取到缓存区中，
但是使用缓存区的话，会导致页面堆积，页面延迟高过，
所以为了避免OpenCv缓存区视频流堆积的情况，
可以使用线程实时读取OpenCv画面，将读取的每一帧内容存在队列中，
在需要获取帧画面时，获取队列中的数据。
"""

