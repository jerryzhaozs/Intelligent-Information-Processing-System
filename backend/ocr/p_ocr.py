from paddleocr import PaddleOCR, draw_ocr
import sys
import os
def getText(x):
    # 获取当前脚本的绝对路径
    current_path = os.path.abspath(__file__)

    # 获取当前脚本所在目录的路径
    current_dir = os.path.dirname(current_path)

    # 将上一层文件夹的路径添加到sys.path中
    parent_dir = os.path.join(current_dir, '..')
    sys.path.append(parent_dir)

    # 引入../tool/test.py文件
    from tool.getLatestFile import getLatestFile
    # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
    # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
    filePath=getLatestFile(1)
    if filePath==-1:
        return '请先上传图片'
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    # img_path = 'C:\\Users\\Administrator\\Desktop\\picture19.png'
    result = ocr.ocr(filePath, cls=True)
    print('ok')
    ans=''
    ans2=[]
    print(len(result))
    if len(result)<1:
        return ''
    for line in result[0]:
        print(type(line[1][0]))
        print(line[1][0])
        ans+=line[1][0]+' '
        ans2.append(line[1][0])
    
    if x==1:
        return ans
    else:
        return ans2
    # result = ocr.ocr(img_path, cls=True)
    # for line in result:
    #     print(type(line[0][1][0]))
    #     print(line[0][1][0])