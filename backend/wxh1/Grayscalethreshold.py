import os
import cv2
import numpy as np
from bayes_opt import BayesianOptimization

# 定义目标函数
def threshold_func(img, block_size, C):
    if block_size % 2 == 0:
        return 0.0
    if block_size < img.shape[0] and block_size < img.shape[1]:
        # 中值滤波
        img = cv2.medianBlur(img,5)
        adaptive_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, C)
        pix_var = np.var(adaptive_threshold)
        return pix_var
    else:
        return 0.0

# 将贝叶斯优化器封装为一个函数
def bayesian_optimization(img):
    # 定义参数搜索范围
    pbounds = {'block_size': (5, 100), 'C': (-20, 20)}

    # 定义贝叶斯优化器
    optimizer = BayesianOptimization(
        f=lambda block_size, C: threshold_func(img=img, block_size=int(block_size), C=int(C)),
        pbounds=pbounds,
        random_state=1,
    )

    # 进行优化
    optimizer.maximize(
        init_points=10, # 初始采样点数量
        n_iter=30, # 迭代次数
    )

    # 获取最佳参数
    best_params = optimizer.max['params']
    max_var_block_size = int(best_params['block_size'])
    max_var_c = int(best_params['C'])
    max_var = optimizer.max['target']

    return max_var_block_size, max_var_c,max_var

# input_folder = 'D:/machine learning/Course design/CBSD68/'
# output_folder = '.'

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# 遍历文件夹
# for root, dirs, files in os.walk(input_folder):
#     for file in files:
#         if file.endswith('.png'):
            # 读取图像
def gth(img_path,out_path):
    img = cv2.imread(img_path, 0)

    # 进行贝叶斯优化
    best_block_size, best_c, best_var = bayesian_optimization(img)
    print(f"图片文件名：{img_path} 最优块大小：{best_block_size} 最优偏移量：{best_c} 方差：{best_var}")

    # 对图像进行自适应灰度分析
    adaptive_threshold_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, best_block_size, best_c)

    # 保存结果
    cv2.imwrite(out_path, adaptive_threshold_img)