import os
import datetime

def getLatestFile(num):
    folder_path = 'C:\\Users\\Administrator\\Desktop\\sys\\server\\static\\pic'

    # 获取文件夹中所有文件的路径和修改时间
    file_paths = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            modified_time = os.path.getmtime(file_path)
            file_paths.append((file_path, modified_time))

    # 根据修改时间对文件路径进行排序
    file_paths.sort(key=lambda x: x[1], reverse=True)

    # 获取最后修改的两个文件的路径
    last_modified_files = []
    for i in range(min(len(file_paths), num)):
        last_modified_files.append(file_paths[i][0])

    # 输出最后修改的两个文件的路径
    if len(last_modified_files)<1:
        if num==1:
            return -1
        else:
            return -1,-1
    if num==1:
        return last_modified_files[0]
    else:
        if len(last_modified_files)<2:
            return last_modified_files[0],last_modified_files[0]
        return last_modified_files[0],last_modified_files[1]