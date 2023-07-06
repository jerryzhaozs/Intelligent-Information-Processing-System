import os
import shutil
def init():
    with open('C:\\Users\\Administrator\\Desktop\\sys\\server\\static\\text\\saved.txt', 'w') as file:
        file.truncate(0)

    folder_path = "C:\\Users\\Administrator\\Desktop\\sys\\server\\static\\pic"  # 文件夹的路径
    shutil.rmtree(folder_path)
    os.mkdir('C:\\Users\\Administrator\\Desktop\\sys\\server\\static\\pic')
