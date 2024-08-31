# Untitled - By: Lenovo - 星期六 7月 8 2023

import sensor, image, time, pyb
from pyb import UART,LED
from pyb import Pin
from pyb import Timer
import json
import ustruct

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time=2000)  # 跳帧
sensor.set_auto_gain(False)  # 关闭自动增益
sensor.set_auto_whitebal(False)  # 关闭白平衡
clock = time.clock()


# 颜色阈值
green_threshold = [(21, 48, -44, 14, 39, 16),
                   (23, 43, -49, -22, 37, 16)]

blue_threshold = [(31, 66, -37, -9, 5, -32),
                   (23, 54, -10, -99, -29, 6)]
blue_threshold_01 = (36, 56, -34, 2, -45, -12)

yellow_threshold = (50, 78, -54, 108, 20, 78)

red_threshold = [ (51, 17, 48, 3, 42, -4),
                  (35, 11, 41, 6, 52, -1),
                  (20, 58, -41, 11, -14, 35), # 有光
                  (8, 40, -39, 10, -10, 20), # 暗
                  (19, 45, 19, 41, 30, -13)]
red_threshold_01 = (19, 45, 19, 41, 30, -13)

# 按键切换
key1 = 0

P7_State = 2
P8_State = 2

# 设置pin1为输入口
pin1 = Pin('P1', Pin.IN, Pin.PULL_UP)
P7_Out = Pin('P7',Pin.OUT_PP)  # P7设置成推挽输出
P8_Out = Pin('P8',Pin.OUT_PP)  # P8设置成推挽输出

tim = Timer(2, freq=1)      # 1hz,1s检测一次

def tick(timer):      #这里开启了一个定时器
    global key1, P7_State, P8_State
    key1 = pin1.value()
    P7_State = P7_Out.value()  # 获取P7的引脚状态，0 or 1
    P8_State = P8_Out.value()  # 获取P8的引脚状态，0 or 1


tim.callback(tick)


#定义寻找色块面积最大的函数
def find_max(blobs):
    max_size=0
    for blob in blobs:
        if blob.pixels() > max_size:
            max_blob=blob
            max_size = blob.pixels()
    return max_blob




if __name__ == "__main__":
    # 真01，假10，敌方10
    while True:
        clock.tick()
        img = sensor.snapshot()
        if key1 == 1:
            for r in img.find_rects(threshold=10000):
                area = r.rect()  # 检测到矩形
                blobs_blue = img.find_blobs([blue_threshold_01], roi = area)
                if blobs_blue:
                    # 在矩形内检测到蓝色，说明是己方宝藏
                    blobs_yellow = img.find_blobs([yellow_threshold], roi = area)
                    # 在矩形框内内检测黄色色块
                    if blobs_yellow:
                        img.draw_rectangle(r.rect(), color = (0, 0, 255))
                        # 在检测到的真宝藏上画红框
                        P7_Out.low()   # 设置p_out引脚为低
                        P8_Out.high()  # 设置p_out引脚为高
                        print("真宝藏", P7_State, P8_State)
                    else:
                        for blob_green in img.find_blobs(green_threshold, roi = area):
                            if blob_green and blob_green.density() > 0.45 and blob_green.density() < 0.60 :
                                img.draw_cross(blob_green.cx(), blob_green.cy())
                                # 在三角形上画十字
                                img.draw_rectangle(r.rect(), color = (255, 255, 255))
                                # 在检测到的假宝藏上画白框
                                P7_Out.high()  # 设置p_out引脚为高
                                P8_Out.low()   # 设置p_out引脚为低
                                print("假宝藏", P7_State, P8_State)
                else:
                    blobs_red = img.find_blobs([red_threshold_01], roi = area)
                    if blobs_red:
                        # 没检测到蓝色,检测到红色，说明是敌方宝藏
                        P7_Out.high()  # 设置p_out引脚为低
                        P8_Out.low()   # 设置p_out引脚为低
                        print("敌方宝藏", P7_State, P8_State)

        else:
            for r in img.find_rects(threshold=10000):
                area = r.rect()  # 检测到矩形
                blobs_red = img.find_blobs([red_threshold_01], roi = area)
                if blobs_red:
                    # 在矩形内检测到红色，说明是己方宝藏
                    blobs_yellow = img.find_blobs([yellow_threshold], roi = area)
                    # 在矩形框内内检测黄色色块
                    if blobs_yellow:
                        img.draw_rectangle(r.rect(), color = (255, 0, 0))
                        # 在检测到的真宝藏上画红框
                        P7_Out.low()   # 设置p_out引脚为低
                        P8_Out.high()  # 设置p_out引脚为高
                        print("真宝藏", P7_State, P8_State)
                    else:
                        for blob_green in img.find_blobs(green_threshold, roi = area):
                            if blob_green and blob_green.density() > 0.45 and blob_green.density() < 0.60 :
                                img.draw_cross(blob_green.cx(), blob_green.cy())
                                # 在三角形上画十字
                                img.draw_rectangle(r.rect(), color = (255, 255, 255))
                                # 在检测到的假宝藏上画白框
                                P7_Out.high()  # 设置p_out引脚为高
                                P8_Out.low()   # 设置p_out引脚为低
                                print("假宝藏", P7_State, P8_State)
                else:
                    blobs_blue = img.find_blobs([blue_threshold_01], roi = area)
                    if blobs_blue:
                        # 没检测到红色,检测到蓝色，说明是敌方宝藏
                        P7_Out.high()  # 设置p_out引脚为低
                        P8_Out.low()  # 设置p_out引脚为低
                        print("敌方宝藏", P7_State, P8_State)
