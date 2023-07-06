import os
import cv2 as cv
import numpy as np
# 合并分裂
# 判断是否需要继续分割
def Division_Judge(img, h0, w0, h, w):
    area = img[h0:h0+h, w0:w0+w]
    mean = np.mean(area)
    std = np.std(area, ddof=1)

    total_points = 0
    operated_points = 0

    for row in range(area.shape[0]):
        for col in range(area.shape[1]):
            if (area[row][col] - mean) < 2 * std:
                operated_points += 1
            total_points += 1

    if operated_points / total_points >= 0.95:
        return True
    else:
        return False

# 合并像素
def Merge(img, h0, w0, h, w):
    for row in range(h0, h0+h):
        for col in range(w0, w0+w):
            if img[row, col] > 100 and img[row, col] < 200:
                img[row, col] = 0
            else:
                img[row, col] = 255

# 递归处理
def Recursion(img, h0, w0, h, w):
    if not Division_Judge(img, h0, w0, h, w) and min(h, w) > 5:
        Recursion(img, h0, w0, int(h/2), int(w/2))
        Recursion(img, h0, w0+int(w/2), int(h/2), int(w/2))
        Recursion(img, h0+int(h/2), w0, int(h/2), int(w/2))
        Recursion(img, h0+int(h/2), w0+int(w/2), int(h/2), int(w/2))
    else:
        Merge(img, h0, w0, h, w)

# 图片分割处理
def Division_Merge_Segmented(file_path, save_folder_path):
    # 读取图片
    img = cv.imread(file_path, cv.IMREAD_GRAYSCALE)

    # 分割图片
    Recursion(img, 0, 0, img.shape[0], img.shape[1])

    # 删除空白区域
    img = img[1:-1, 1:-1]  # 删除边缘
    return img
    # 保存分割后的图片
    # file_name = os.path.basename(file_path)
    # new_file_path = os.path.join(save_folder_path, "processed_" + file_name)
    # return new_file_path
    # cv.imwrite(new_file_path, img, [cv.IMWRITE_PNG_COMPRESSION, 0])

    # # 删除旧的文件
    # old_file_path = os.path.join(save_folder_path, "processed_" + "processed_" + file_name)
    # if os.path.exists(old_file_path):
    #     os.remove(old_file_path)

# 获取指定目录下的所有图片文件路径列表
def get_image_files(path):
    files = os.listdir(path)
    image_files = []
    for file in files:
        full_path = os.path.join(path, file)
        if os.path.splitext(full_path)[-1].lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
            image_files.append(full_path)
    return image_files

# if __name__ == "__main__":
def sm_method(file_path):
    # 指定要处理的文件夹路径
    # folder_path = "D:/machine learning/Course design/CBSD68"

    # # 分割后的图片保存到这个目录中
    # save_folder_path = "D:/machine learning/Course design/split_merger_output"
    # if not os.path.exists(save_folder_path):
    #     os.mkdir(save_folder_path)

    # # 获取所有图片文件的路径
    # image_files = get_image_files(folder_path)

    # # 对每个图片文件进行分割处理
    # for file_path in image_files:
    ans = Division_Merge_Segmented(file_path, 'save_folder_path')
    return ans