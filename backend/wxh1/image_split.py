import cv2
import numpy as np
from PIL import Image, ImageOps
def image_split(img):
    # height, width = img.shape[:2]
    # border_size = 10
    # white = (255, 255, 255)
    # img[0:border_size, :] = white
    # img[height - border_size:height, :] = white
    # img[:, 0:border_size] = white
    # img[:, width - border_size:width] = white
    
  #  cv2.imwrite("modified_image.jpg", img)
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # 对灰度图像进行二值化处理
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 建立一个三=3*3矩阵
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 进行噪声去除操作
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    #膨胀两次，背景
    sure_bg = cv2.dilate(opening, kernel, iterations=2)

    #腐蚀两次，前景
    sure_fg = cv2.erode(opening, kernel, iterations=2)

    # 确定未知区域
    unknown = cv2.subtract(sure_bg, sure_fg)

    # 进行距离变换算法，返回图片每个像素点的值为离他最近的背景距离，使前景每个物体中心更亮，使每个物体相对独立
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

    # 对距离变换图像进行归一化处理，使物体与物体直接的灰度变暗，不同物体分的更开，从而画出轮廓
    cv2.normalize(dist_transform, dist_transform, 0, 1.0, cv2.NORM_MINMAX)

    # 确定前景区域，通过阈值为dist_transform.max的一半及最亮的点到背景的距离的一半以下的区域视为背景，以内视为前景
    ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)

    # 确定未知区域
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # 进行标记操作，计算出来前景区域中有几个独立的物体
    ret, markers = cv2.connectedComponents(sure_fg)

    # 对标记进行更改
    markers = markers + 1#要用0表示分水岭区域，所以要防止背景为0
    markers[unknown == 255] = 0#将不确定区域中的像素点为255的点标记为0
    markers_copy = markers.copy()
    markers_copy[markers == 0] = 150  # 灰色表示分水岭
    markers_copy[markers == 1] = 0  # 黑色表示背景
    markers_copy[markers > 1] = 255  # 白色表示前景
    markers_res = markers.copy()
    markers_copy = np.uint8(markers_copy)




    # 使用分水岭算法对图像进行分割，-1表示边界来分离不同的物体
    markers = cv2.watershed(img, markers)
    # markers = np.uint8(markers)

  #  cv2.imwrite('markers.jpg',  markers_copy)
   # img[markers == -1] = [0, 0, 255]
    # 将结果图像保存
  #  cv2.imwrite('splited.jpg', img)

    black_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    black_img[markers==-1]=255
   # cv2.imwrite('splited.jpg', black_img)

    # kernel = np.ones((5, 5), np.uint8)
    # dilated = cv2.dilate(black_img, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(black_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print(img.shape[0] * img.shape[1] * 8 / 10)
    new_contours = []

    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        count = 0
        for j in range(i+1,len(contours)):
            if i != j:
                if area == cv2.contourArea(contours[j]):
                    count += 1
        if count == 0:
            new_contours.append(contours[i])

    filtered_contours = []

    for cnt in new_contours:
        area = cv2.contourArea(cnt)
        if area <img.shape[0]* img.shape[1]*9/10:
            filtered_contours.append(cnt)

        black_img2 = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
        cv2.drawContours(black_img2, filtered_contours, -1, (255, 255, 255), 3)
     #   cv2.imwrite('contours.jpg', black_img2)
    #
    # for i, contour in enumerate(filtered_contours):
    #     print('Contour {}:'.format(i))
    #     print(' - Area: {:.2f}'.format(cv2.contourArea(contour)))
    #     print(' - Perimeter: {:.2f}'.format(cv2.arcLength(contour, True)))
    #     print(' - Bounding box: {}'.format(cv2.boundingRect(contour)))
    #     print(' - Minimum enclosing circle: {}'.format(cv2.minEnclosingCircle(contour)))
    #     print('')

    return img,filtered_contours
