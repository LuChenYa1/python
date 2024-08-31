import cv2
import math
import numpy as np
#import matplotlib.pyplot as plt

class BBox(object):

    def __init__(self, bbox):
        self.left = bbox[0]
        self.top = bbox[1]
        self.right = bbox[2]
        self.bottom = bbox[3]

def Img_Outline(input_dir):
    original_img = input_dir
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_img, (9, 9), 0)                     # 高斯模糊去噪（设定卷积核大小影响效果）

    _, RedThresh = cv2.threshold(blurred, 165, 255, cv2.THRESH_BINARY)  # 设定阈值165（阈值影响开闭运算效果） //200效果最好   当前无影响165


    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))          # 定义矩形结构元素
    closed = cv2.morphologyEx(RedThresh, cv2.MORPH_CLOSE, kernel)       # 闭运算（链接块）
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)           # 开运算（去噪点）
    return original_img, gray_img, RedThresh, closed, opened

def findContours_img(original_img, opened):
    contours, hierarchy = cv2.findContours(opened, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(contours, key=cv2.contourArea, reverse=True)[1]   # 计算最大轮廓的旋转包围盒
    rect = cv2.minAreaRect(c)                                    # 获取包围盒（中心点，宽高，旋转角度）
    box = np.int0(cv2.boxPoints(rect))                           # box
    draw_img = cv2.drawContours(original_img.copy(), [box], -1, (0, 0, 255), 3)
    return box,draw_img

def Perspective_transform(box,original_img):
    # 获取画框宽高(x=orignal_W,y=orignal_H)
    orignal_W = math.ceil(np.sqrt((box[3][1] - box[2][1])**2 + (box[3][0] - box[2][0])**2))
    orignal_H= math.ceil(np.sqrt((box[3][1] - box[0][1])**2 + (box[3][0] - box[0][0])**2))

    # 原图中的四个顶点,与变换矩阵
    pts1 = np.float32([box[0], box[1], box[2], box[3]])
    pts2 = np.float32([[int(orignal_W+1),int(orignal_H+1)], [0, int(orignal_H+1)], [0, 0], [int(orignal_W+1), 0]])

    # 生成透视变换矩阵；进行透视变换
    M = cv2.getPerspectiveTransform(pts1, pts2)
    result_img = cv2.warpPerspective(original_img, M, (int(orignal_W+3),int(orignal_H+1)))

    return result_img

def resize_keep_aspectratio(image_src, dst_size):
    src_h, src_w = image_src.shape[:2]
    print(src_h, src_w)
    dst_h, dst_w = dst_size

    # 判断应该按哪个边做等比缩放
    h = dst_w * (float(src_h) / src_w)  # 按照ｗ做等比缩放
    w = dst_h * (float(src_w) / src_h)  # 按照h做等比缩放

    h = int(h)
    w = int(w)

    if h <= dst_h:
        image_dst = cv2.resize(image_src, (dst_w, int(h)))
    else:
        image_dst = cv2.resize(image_src, (int(w), dst_h))

    h_, w_ = image_dst.shape[:2]
    print(h_, w_)

    top = int((dst_h - h_) / 2)
    down = int((dst_h - h_ + 1) / 2)
    left = int((dst_w - w_) / 2)
    right = int((dst_w - w_ + 1) / 2)

    value = [0, 0, 0]
    borderType = cv2.BORDER_CONSTANT
    print(top, down, left, right)
    image_dst = cv2.copyMakeBorder(image_dst, top, down, left, right, borderType, None, value)

    return image_dst


if __name__=="__main__":
    global DPI
    DPI = 0.00245

    input_dir = "images/migong1.png"
    cap = cv2.VideoCapture(1)

    while (cap.isOpened()):
        ret, frame = cap.read()
        img0 = frame
        original_img, gray_img, RedThresh, closed, opened = Img_Outline(img0)
        box, draw_img = findContours_img(original_img, opened)
        cv2.imshow('draw_img', draw_img)
        result_img = Perspective_transform(box, original_img)

        size = result_img.shape
        w = size[1]
        h = size[0]

        if w < h:
            img90 = np.rot90(result_img)
            # cv2.imshow("img90", img90)
        else:
            img90 = result_img
        img90_canndy = cv2.Canny(img90, 30, 150)

        w = 20
        h = 5
        params = cv2.SimpleBlobDetector_Params()
        params.filterByArea = True
        params.minArea = 10e1
        params.maxArea = 10e2
        params.minDistBetweenBlobs = 25
        params.filterByConvexity = False

        gray = cv2.cvtColor(img90, cv2.COLOR_BGR2GRAY)
        minThreshValue = 120
        _, gray = cv2.threshold(gray, minThreshValue, 255, cv2.THRESH_BINARY)
        gray = cv2.resize(gray, dsize=None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        img90_resize = cv2.resize(img90, dsize=None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(gray)
        im_with_keypoints = cv2.drawKeypoints(gray, keypoints, np.array([]), (255, 0, 0),
                                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        color_img = cv2.cvtColor(im_with_keypoints, cv2.COLOR_BGR2RGB)

        size = color_img.shape
        w = size[1]
        h = size[0]

        for i in range(0, len(keypoints)):
            print(keypoints[i].pt[0], keypoints[i].pt[1])

        get_persent_x = w / 12 - 0.7675
        get_persent_y = h / 10 - 0.585
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 0, 255)
        thickness = 2
        font_scale = 1
        point_image = color_img.copy()

        for i in range(0, len(keypoints)):
            if keypoints[i].pt[0] / get_persent_x != 0:
                pointx_now = int(keypoints[i].pt[0] / get_persent_x) + 1
            else:
                pointx_now = int(keypoints[i].pt[0] / get_persent_x)

            if keypoints[i].pt[1] / get_persent_y != 0:
                pointy_now = int(keypoints[i].pt[1] / get_persent_y) + 1
            else:
                pointy_now = int(keypoints[i].pt[1] / get_persent_y)
            print(pointx_now, pointy_now)
            text_x = str(pointx_now)
            text_y = str(pointy_now)
            text = "(" + text_x + "," + text_y + ")"
            cv2.putText(point_image, text, (int(keypoints[i].pt[0]), int(keypoints[i].pt[1])), font, font_scale, color,
                        thickness)

        cv2.imshow('point_image', point_image)
        cv2.imshow('original_img', original_img)
        c = cv2.waitKey(1)
        if c == ord('q'):
            break

cv2.waitKey(0)
cv2.destroyAllWindows()









