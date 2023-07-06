import sys
import os

# 获取当前文件所在目录的绝对路径
current_path = os.path.abspath(os.path.dirname(__file__))

# 获取当前文件所在目录的上级目录的绝对路径
# parent_path = os.path.abspath(os.path.join(current_path, '..'))

# 将同层级目录的路径添加到 sys.path 中
sys.path.append(current_path)
from translate import get_input,get_ans
# C:\Users\Administrator\Desktop\sys\server\trans\trans2\translate.py
# while True:
#     seq=input()
#     flag, seq = get_input(seq)
#     ans=get_ans(seq)
#     print(ans)

def getEn2(text):
    flag,seq=get_input(text)
    ans=get_ans(seq)
    return ans