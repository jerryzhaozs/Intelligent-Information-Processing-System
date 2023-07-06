from PIL import Image
import cv2
import random
import re
import numpy as np
import sys
sys.path.append('..')
from tool.getLatestFile import getLatestFile
from .image_algebraic_operations import image_algebraic_operations_add,image_algebraic_operations_cut,image_algebraic_operations_multiply,image_algebraic_operations_division
from .image_logical_operations import and_operator,not_operator,or_operator,xor_operator
from .image_geometric_transformation import image_translate,image_affine,image_crop,image_flip,image_rotate,image_scale
from .image_shadow_removal import getRemoval
from .Grayscalethreshold import gth
from .filtering import high_pass_filter,low_pass_filter
from .Fourier import  fourier
from .yxl_regional_growth import rg_method
from .yxl_split_merger import sm_method
def image_allkindsofchange (path1,path2,resultpath,command,x):
    path1,path2=getLatestFile(2)
    if path2==-1:
        return -1
    resultpath=f'C://Users//Administrator//Desktop//sys//server//static//pic//'
    # 提取command中的数字信息
    pattern = r"\d+\.\d+|\d+"
    temp = re.findall(pattern, command)
    num_list = []
    for r in temp:
        num_list.append(float(r))
    # 打开图片
    # img1 = Image.open(path1)
    # img2 = Image.open(path2)
    # img1=cv2.imread(path1)
    # img2=cv2.imread(path2)
    # #找到大图小图
    # width1, height1 = img1.size
    # width2, height2 = img2.size
    # if width1 * height1 > width2 * height2:
    #     width = width1
    #     height = height1
    #     img_big = img1.convert('RGB')  # 转换格式为RGB
    #     img_small = img2.convert('RGB')
    # else:
    #     width = width2
    #     height = height2
    #     img_big = img2.convert('RGB')
    #     img_small = img1.convert('RGB')
    # #统一大小
    # img_white = Image.new('RGB', (width, height), color='white')
    # offset_x = int((img_white.width - img_small.width) / 2)
    # offset_y = int((img_white.height - img_small.height) / 2)
    # img_white.paste(img_small, (offset_x, offset_y))



    # # 将 PIL.Image 转为 NumPy 数组
    # np_big = np.array(img_big)
    # np_small = np.array(img_white)
    # img1=np.array(img1)
    # img2=np.array(img2)
        # 读取两张图片
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    # 获取图片的宽度和高度
    height1, width1, _ = img1.shape
    height2, width2, _ = img2.shape
    if width1> width2:
        width = width1
        width_s=width2
    else:
        width = width2
        width_s = width1
    if  height1 > height2:
        height = height1
        height_s=height2
    else:
        height = height2
        height_s = height1

    # if width1 * height1 > width2 * height2:
    #     width = width1
    #     height = height1
    #     np_big = img1
    #     np_small = img2
    # else:
    #     width = width2
    #     height = height2
    #     np_big = img2
    #     np_small = img1



    # 创建白色底图
    img1_white = 255 * np.ones((height, width, 3), dtype=np.uint8)
    img2_white = 255 * np.ones((height, width, 3), dtype=np.uint8)
    # 
    # offset_x = int((width - width_s) / 2)
    # offset_y = int((height - height_s) / 2)

    # 在底图上粘贴小图
    img1_white[int((height-img1.shape[0])/2):(int((height-img1.shape[0])/2)+img1.shape[0]),int((width-img1.shape[1])/2):(int((width-img1.shape[1])/2)+img1.shape[1]) ] =  img1
    img2_white[int((height-img2.shape[0])/2):(int((height-img2.shape[0])/2)+img2.shape[0]),int((width-img2.shape[1])/2):(int((width-img2.shape[1])/2)+img2.shape[1]) ] =  img2
    img1= img1_white
    img2 = img2_white
    #测试代数运算
    if x==6.0:
        if len(num_list)<2:
            a=0.5
            b=0.5
        else:
            a=num_list[0]
            b=num_list[1]
            c=a+b
            a=a/c
            b=b/c
        res=image_algebraic_operations_add(img1,img2,a,b)
    if x==6.1:
        res=image_algebraic_operations_cut(img1,img2)
    if x==6.2:
        res=image_algebraic_operations_multiply(img1,img2)
    if x == 6.3:
        res=image_algebraic_operations_division(img1,img2)

        #测试逻辑运算
    if x == 6.4:
        res=and_operator(img1,img2)
    if x == 6.5:
        res=or_operator(img1,img2)
    if x == 6.6:
        res=not_operator(img1)
    if x == 6.7:
        res=xor_operator(img1,img2)

        #测试几何变换
    if x == 6.8:
        if len(num_list)<2:
            return "e需要至少2个参数"
        now=cv2.imread(path1)
        res=image_translate(now,num_list[0],num_list[1])
    if x == 6.9:
        if len(num_list)<1:
            return "e需要至少1个参数"
        now=cv2.imread(path1)
        res=image_rotate(now,num_list[0]%360)
    if x == 7.0:
        if len(num_list)<2:
            return "e需要至少2个参数"
        now=cv2.imread(path1)
        res=image_scale(now,num_list[0],num_list[1])
    if x == 7.1:
        if len(num_list)<1:
            return "e需要至少1个参数"
        now=cv2.imread(path1)
        res=image_flip(now,int(num_list[0])%2)
    if x == 7.2:
        if len(num_list)<4:
            return "e需要至少4个参数"
        now=cv2.imread(path1)
        res=image_crop(now,num_list[0],num_list[1],num_list[2],num_list[3])
    if x == 7.3:
        if len(num_list)<12:
            return "e需要至少12个参数"
        res=image_affine(img1,np.float32([[num_list[0], num_list[1]], [num_list[2], num_list[3]], [num_list[4], num_list[5]]]), np.float32([[num_list[6], num_list[7]], [num_list[8], num_list[9]], [num_list[10], num_list[11]]]))
    if x==7.4:
        random_int = random.randint(1, 100000)
        resultpath=resultpath+(str)(random_int)+'.png'
        getRemoval(path1, resultpath)
        return str(random_int)
    if x==7.5:
        res= fourier(path1,1)
    if x==7.6:
        if len(num_list)<1:
            res= high_pass_filter(path1)
        else:
            res= high_pass_filter(path1,num_list[0])
    if x==7.7:
        if len(num_list)<1:
            res= low_pass_filter(path1)
        else:
            res= low_pass_filter(path1,num_list[0])
    if x==7.9:
        print('?')
        random_int = random.randint(1, 100000)
        resultpath=resultpath+(str)(random_int)+'.png'
        gth(path1, resultpath)
        return str(random_int)
    if x==11:
        res=rg_method(path1)
    if x==12:
        res=sm_method(path1)

    random_int = random.randint(1, 100000)
    resultpath=resultpath+(str)(random_int)+'.png'
    cv2.imwrite(resultpath, res)
    return str(random_int)

# path1='./wxh1/picture16.png'
# path2='./picture17.png'
# path3='./picturef.png'
# command='两图相加 1 2'
# command='两图相加'
# x=7.0
# image_allkindsofchange(path1=path1,path2=path2,resultpath=path3,command=command,x=x)
# image_allkindsofchange(path1, '', 'hehe.png', command, x)