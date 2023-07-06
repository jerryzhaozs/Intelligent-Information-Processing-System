import cv2
import numpy as np
import os

# 区域生长
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

connects = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0),
            Point(1, 1), Point(0, 1), Point(-1, 1), Point(-1, 0)]

def get_dist(seed_location1, seed_location2, im):
    l1 = im[seed_location1.x, seed_location1.y]
    l2 = im[seed_location2.x, seed_location2.y]
    count = np.sqrt(np.sum(np.square(l1-l2)))
    return count

def rgb2gray(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    return gray

def grow_region(image_path, seed_location, threshold):
    im = cv2.imread(image_path)
    im=rgb2gray(im)
    img_mark = np.zeros_like(im[..., 0])
    img_re = np.zeros_like(im)

    height, width, depth = im.shape

    seed_list = []
    seed_list.append(seed_location)

    class_k = 1

    while(len(seed_list) > 0):
        seed_tmp = seed_list[0]
        seed_list = seed_list[1:]

        img_mark[seed_tmp.x, seed_tmp.y] = class_k

        for i in range(8):
            tmpX = seed_tmp.x + connects[i].x
            tmpY = seed_tmp.y + connects[i].y

            if (tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= width):
                continue

            dist = get_dist(seed_tmp, Point(tmpX, tmpY), im)

            if (dist < threshold and img_mark[tmpX, tmpY] == 0):
                img_re[tmpX, tmpY][0] = im[tmpX, tmpY][0]
                img_re[tmpX, tmpY][1] = im[tmpX, tmpY][1]
                img_re[tmpX, tmpY][2] = im[tmpX, tmpY][2]
                img_mark[tmpX, tmpY] = class_k
                seed_list.append(Point(tmpX, tmpY))

    return img_re

def rg_method(image_path):
    # input_folder = 'D:/machine learning/Course design/adaptive_output_'
    # output_folder = 'D:/machine learning/Course design/growing_output_'
    seed_location = Point(15, 15)
    threshold = 3

    # 创建输出文件夹，如果不存在
    # if not os.path.exists(output_folder):
    #     os.makedirs(output_folder)

    # 遍历图像文件
        # for filename in os.listdir(input_folder):
        #     image_path = os.path.join(input_folder, filename)
        #     output_path = os.path.join(output_folder, filename)

# 进行区域生长
    img_re = grow_region(image_path, seed_location, threshold)

# 保存输出图像
    # cv2.imwrite(output_path, img_re)
    return img_re
# path='C:\\Users\\Administrator\\Desktop\\picture18.png'
# a=rg_method(path)
# cv2.imwrite('ok.png', a)