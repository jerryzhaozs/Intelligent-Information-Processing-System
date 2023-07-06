import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
sys.path.append('..')
from .Fourier import fourier

def low_pass_filter(path, filter_size=30):
    filter_size=int(filter_size)
    """
    低通滤波函数
    :param img_path: 图像路径
    :param filter_size: 滤波器大小，默认为30
    :return: 滤波后的图像
    """
    # 读取图像
    img = cv2.imread(path, 0)

    fshift = fourier(path,2)

    # 构建低通滤波器并进行滤波
    rows, cols = img.shape
    crow, ccol = int(rows/2), int(cols/2)
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow-filter_size:crow+filter_size, ccol-filter_size:ccol+filter_size] = 1
    fshift_low = fshift * mask
    img_back_low = np.fft.ifft2(np.fft.ifftshift(fshift_low))
    img_back_low = np.abs(img_back_low)

    return img_back_low


def high_pass_filter(path, filter_size=10):
    filter_size=int(filter_size)
    """
    高通滤波函数
    :param img_path: 图像路径
    :param filter_size: 滤波器大小，默认为10
    :return: 滤波后的图像
    """
    # 读取图像
    img = cv2.imread(path, 0)

    # 进行傅里叶变换
    fshift = fourier(path,2)

    # 构建高通滤波器并进行滤波
    rows, cols = img.shape
    crow, ccol = int(rows/2), int(cols/2)
    mask = np.ones((rows, cols), np.uint8)
    mask[crow-filter_size:crow+filter_size, ccol-filter_size:ccol+filter_size] = 0
    fshift_high = fshift * mask
    img_back_high = np.fft.ifft2(np.fft.ifftshift(fshift_high))
    img_back_high = np.abs(img_back_high)

    return img_back_high
# img_low = low_pass_filter('example.jpg', 30)
# img_high = high_pass_filter('example.jpg',5)
#
# plt.subplot(131), plt.imshow(cv2.imread('example.jpg', 0), cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(132), plt.imshow(img_low, cmap='gray')
# plt.title('Low Pass Filtered Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(133), plt.imshow(img_high, cmap='gray')
# plt.title('High Pass Filtered Image'), plt.xticks([]), plt.yticks([])
# plt.show()
