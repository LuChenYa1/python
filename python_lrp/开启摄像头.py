import cv2

# 开启摄像头
cap = cv2.VideoCapture(0)

# 摄像头是开启状态则不断刷新进入循环
while(cap.isOpened()):
    ret, frame = cap.read()  # 读取帧画面
    # 防止读取失败
    while not ret:
        ret, frame = cap.read()
    cv2.imshow('Video', frame)  # 显示画面

    if cv2.waitKey(1) >= 2:     # 等待输入任意数字按键，结束
        break
    # key = cv2.waitKey(1)
    # if key == ord('q') or key == ord('w'):  # 输入q或者w
    #     break
# 释放摄像头资源、窗口
cap.release()
cv2.destroyAllWindows()