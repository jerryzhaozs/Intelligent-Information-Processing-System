import cv2
import numpy as np
import matplotlib.pyplot as plt

def fourier (path,back_type):
# 读取图片并转换为灰度图像

    # 读取图片并转换为灰度图像
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# 进行二维傅里叶变换
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)

# 构建振幅谱图
    magnitude_spectrum = 20 * np.log(np.abs(fshift))


    # return magnitude_spectrum
    if back_type==1:
        return magnitude_spectrum
    else:
        print('返回2')
        return fshift

# 绘制原始图像和傅里叶变换后的频谱图像
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(fshift, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()
# path='C:\\Users\\Administrator\\Desktop\\picture13.jpg'
# a=fourier(path)
# cv2.imwrite('ok.png', a)