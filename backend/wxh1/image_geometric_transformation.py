import cv2
import numpy as np

def image_translate(img,a,b):
    # 定义平移矩阵，x轴方向平移100个像素，y轴方向平移50个像素
    M = np.float32([[1, 0, a], [0, 1, 50]])
    # 进行平移变换操作
    rows, cols = img.shape[:2]
    img_translated = cv2.warpAffine(img, M, (cols, rows))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_translated
def image_rotate(img, angle):
    # 定义旋转中心为图像中心
    rows, cols = img.shape[:2]
    center = (cols / 2, rows / 2)
    # 构造旋转矩阵，参数2为旋转角度，参数3为旋转缩放比例
    M = cv2.getRotationMatrix2D(center, angle, 1)
    # 进行旋转变换操作
    img_rotated = cv2.warpAffine(img, M, (cols, rows))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_rotated
def image_scale(img, fx, fy):
    # 进行缩放变换操作
    img_scaled = cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_LANCZOS4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_scaled
def image_flip(img, flip_code):
    # 进行翻转变换操作
    flip_code=int(flip_code)
    img_flipped = cv2.flip(img, flipCode=flip_code)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_flipped
def image_crop(img, x1, y1, x2, y2):
    # 检查剪切区域是否合法
    if y1 >= y2 or x1 >= x2:
        y1=y2
        x1=x2
        raise ValueError('裁剪区域超出大小')
    # 进行裁剪操作
    x2=min(x2,img.shape[1])
    y2=min(y2,img.shape[0])
    y1=int(y1)
    y2=int(y2)
    x1=int(x1)
    x2=int(x2)
    img_cropped = img[y1:y2, x1:x2]
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_cropped
def image_affine(img, src_pts, dst_pts):
    # 检查参数是否合法
    if len(src_pts) != 3 or len(dst_pts) != 3:
        raise ValueError('点的数量错误')
    if not all(len(pt) == 2 for pt in src_pts + dst_pts):
        raise ValueError('请输入正确的坐标')

    # 计算仿射变换矩阵
    M = cv2.getAffineTransform(src_pts, dst_pts)

    # 进行仿射变换操作
    img_affine = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_affine

