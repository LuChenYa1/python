# Untitled - By: Lenovo - 星期六 7月 8 2023

import sensor, image, time, pyb
from pyb import UART,LED
from pyb import Pin
from pyb import Timer
import json
import ustruct

LED_R = pyb.LED(1) # Red LED = 1, Green LED = 2, Blue LED = 3, IR LEDs = 4.
LED_G = pyb.LED(2)
LED_B = pyb.LED(3)

LED_R.on()
LED_G.on()
LED_B.on()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time=2000)  # 跳帧
sensor.set_auto_gain(False)  # 关闭自动增益
sensor.set_auto_whitebal(False)  # 关闭白平衡
clock = time.clock()

LED_R.off()
LED_G.off()
LED_B.off()

# 颜色阈值
# red_threshold = (37, 50, 37, 62, 11, 44
# green_threshold = (20, 30, -98, 97, -68, 47)
# (0, 15, 0, 40, -80, -20)] # generic_blue_thresholds
blue_threshold = (31, 66, -37, -9, 5, -32)
yellow_threshold = (50, 78, -54, 108, 20, 78)
red_threshold = (51, 17, 48, 3, 42, -4)
red_threshold_01 = (35, 11, 41, 6, 52, -1)
blue_threshold_01 = (23, 54, -10, -99, -29, 6)

# 测距常数
k = 950

# 按键切换
key1 = 0

# 设置pin1为输入口
pin1 = Pin('P1', Pin.IN, Pin.PULL_UP)

uart = UART(3,115200)   #定义串口3变量，设置波特率
uart.init(115200, bits=8, parity=None, stop=1) # init with given parameters

def tick(timer):      #这里开启了一个定时器
    global key1
    key1 = pin1.value()

tim = Timer(2, freq=1)      # 1hz,1s检测一次
tim.callback(tick)


#定义寻找色块面积最大的函数
def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob.pixels() > max_size:
            max_blob=blob
            max_size = blob.pixels()
    return max_blob

# 发送数据函数
def send_data_packet(x, y):
    temp = ustruct.pack("<bbhhb",                #格式为俩个字符俩个整型
                   0x2C,                       #帧头1
                   0x12,                       #帧头2
                   int(x), # up sample by 2    #数据1
                   int(y), # up sample by 2    #数据2
                   0x5B)
    uart.write(temp);                           #串口发送

while True:
    clock.tick()
    img = sensor.snapshot()
    if key1 == 0:
        for r in img.find_rects(threshold=10000):
            area = r.rect()  # 检测到矩形
            blobs_blue = img.find_blobs([blue_threshold_01], roi = area)
            if blobs_blue:
                # 在矩形内检测到蓝色，说明是己方宝藏
                blobs_yellow = img.find_blobs([yellow_threshold], roi = area)
                # 在矩形框内内检测黄色色块
                if blobs_yellow:
                    b = find_max(blobs_yellow)  # 将返回数据赋值给b
                    Lm = (b[2] + b[3]) / 2
                    length = k / Lm
                    print(length)
                    img.draw_rectangle(r.rect(), color = (0, 0, 255))
                    # 在检测到的真宝藏上画红框
                    send_data_packet(length, 1)
                else:
                    img.draw_rectangle(r.rect(), color = (255, 255, 255))
                    # 在检测到的假宝藏上画白框
                    send_data_packet(0, 0)
    else:
        for r in img.find_rects(threshold=10000):
            area = r.rect()  # 检测到矩形
            blobs_red = img.find_blobs([red_threshold_01], roi = area)
            if blobs_red:
                # 在矩形内检测到红色，说明是己方宝藏
                blobs_yellow = img.find_blobs([yellow_threshold], roi = area)
                # 在矩形框内内检测黄色色块
                if blobs_yellow:
                    b = find_max(blobs_yellow)  # 将返回数据赋值给b
                    Lm = (b[2] + b[3]) / 2
                    length = k / Lm
                    print(length)
                    img.draw_rectangle(r.rect(), color = (255, 0, 0))
                    # 在检测到的真宝藏上画红框
                    send_data_packet(length, 1)
                else:
                    img.draw_rectangle(r.rect(), color = (255, 255, 255))
                    # 在检测到的假宝藏上画白框
                    send_data_packet(0, 0)

