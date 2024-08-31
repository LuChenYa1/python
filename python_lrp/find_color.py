import sensor, image, time
from pyb import LED
from pyb import Pin

# 色块阈值
red_threshold = (37, 50, 37, 62, 11, 44)
blue_threshold = (28, 48, 2, 19, -60, -25)
# 配置相机
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)

# 提示点灯
clock = time.clock()
led_red = LED(1)
led_green = LED(2)
led_blue = LED(3)
Pred_out = Pin('P0', Pin.OUT_PP)
Pblue_out = Pin('P6', Pin.OUT_PP)
color_red = 1
color_blue = 2
color_none = 3


def Color_Find(color):
    if color == color_red:
        led_red.on()
        led_blue.off()
        led_green.off()
        Pred_out.high()
        Pblue_out.low()
    elif color == color_blue:
        led_red.off()
        led_blue.on()
        led_green.off()
        Pred_out.low()
        Pblue_out.high()
    else:
        led_green.on()
        led_red.off()
        led_blue.off()
        Pred_out.low()
        Pblue_out.low()


while True:
    clock.tick()
    # 拍照
    img = sensor.snapshot()
    # 寻找色块
    find_red = img.find_blobs([red_threshold])
    find_blue = img.find_blobs([blue_threshold])

    if find_red:
        for b in find_red:
            img.draw_rectangle(b[0:4])
            img.draw_cross(b[5], b[6])
            Color_Find(color_red)
    elif find_blue:
        for b in find_blue:
            img.draw_rectangle(b[0:4])
            img.draw_cross(b[5], b[6])
            Color_Find(color_blue)
            # 外框的中心坐标
    else:
        Color_Find(color_none)

    print(clock.fps())  # 注意: 你的OpenMV连到电脑后帧率大概为原来的一半
    # 如果断开电脑，帧率会增加
