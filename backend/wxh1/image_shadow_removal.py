import cv2
import numpy as np
#include <opencv2/opencv.hpp>
#include <iostream>
from scipy.spatial._ckdtree import cKDTree
from .image_split import image_split


def getRemoval(path,outpath):
    # 读取原始图像并转换为灰度图像
    image = cv2.imread(path)
    
    height, width = image.shape[:2]
    border_size = 10
    white = (169,169,169)
    image[0:border_size, :] = white
    image[height - border_size:height, :] = white
    image[:, 0:border_size] = white
    image[:, width - border_size:width] = white

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    img ,contours=image_split(image)
    no_shadow_pixels = []
    pts = []
    light=[]
    an=0
    for contour in contours:
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                distance = cv2.pointPolygonTest(contour,(j,i), True)
                if distance <-5 and distance >-10 and cv2.pointPolygonTest(contour,(j,i), False)!=1:
                    no_shadow_pixels.append((j,i,gray[i,j]))
                if cv2.pointPolygonTest(contour,(j,i),False) == 1:
                    pts.append([j,i,gray[i,j]])
                # print((i,j))
        # tree = cKDTree(no_shadow_pixels)
        # dist, idx = tree.query(pts)
        # 将距离最近的点的灰度值赋值给pts中的点

    # for i in range(len(pts)):
    #     an = int(gray[no_shadow_pixels[idx[i]][1], no_shadow_pixels[idx[i]][0]])+int(hsv_img[pts[i][1],pts[i][0]][2])
    #     while an>255:
    #         an=255
    #     k=hsv_img[pts[i][1],pts[i][0]][2]/255+0.8
    #     # print(k)
    #     hsv_img[pts[i][1],pts[i][0]][2] = an/k
        brightness_values = [pt[2] for pt in no_shadow_pixels]
        mean_brightness = np.mean(brightness_values)
        print("平均亮度值:", mean_brightness)

        for i in range(len(pts)):
            # an = int(gray[no_shadow_pixels[idx[i]][1], no_shadow_pixels[idx[i]][0]])+int(hsv_img[pts[i][1],pts[i][0]][2])
            # while an>255:
            #     an=255
            k=hsv_img[pts[i][1],pts[i][0]][2]/255+0.5
            end=mean_brightness*k
            while end>255:
                end/=1.3
            # print(k)
            hsv_img[pts[i][1],pts[i][0]][2] = end

    brighter_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    median = cv2.medianBlur(brighter_img, 5)
    cv2.imwrite(outpath,  brighter_img )

# getRemoval('./picture13.jpg','./res.png')