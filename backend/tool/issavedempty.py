import os
def getpara():
    with open('C:\\Users\\Administrator\\Desktop\\sys\\server\\static\\text\\saved.txt', 'r',encoding="utf-8") as f:
        lines = f.readlines()
        num_lines = len(lines)
        if num_lines==0:
            return -1
        else:
            return 1

print(getpara())