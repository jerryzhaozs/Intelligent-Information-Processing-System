from flask import Flask,request
from flask_cors import CORS
from flask import jsonify
from method.commandIdentify import identify
# from ocr.ocr_train import getText
from ocr.p_ocr import getText
# from trans.temp import getEn
from tool.initfile import init
from tool.issavedempty import getpara
from wxh1.image_dispose import image_allkindsofchange
from corrector.correct import correct
from emotion.final_predict import getEmotion
from trans.trans2.go import getEn2
import random


import json
app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/',methods=['POST'])
def go():
    content = request.json['params']['content']
    print(content)
    res=identify(content)
    res=float(res)
    print(res)
    # if res==8:
    #     last=8
    if res==1:
        print('用户输入图片')
        # last=-1
        return 'inputPic'
    if res==3:
        print('用户清空聊天记录')
        # last=-1
        return 'clear'
    if res==2:
        print('识别文字信息')
        reply=getText(1)
        # last=-1
        if reply=='':
            return '识别失败'
        else:
            return reply
    if res==4:
        print('文字信息中译英')
        reply=getText(2)
        
        out=''
        for r in reply:
            # if last==8:
            #     thisnow=correct(r)
            thisnow=getEn2(r)
            out+=thisnow+' '
        # reply=getEn2(reply)
        # last=-1
        return out
    if res==5:
        print('对文字进行情感分析')
        reply=getText(1)
        # last=-1
        if reply=='':
            return '识别失败'
        else:
            return '包含的感情有：'+getEmotion(reply)
    if res==8:
        print('对文字进行纠错')
        reply=getText(2)
        # reply=corrector(reply)
        if reply=='': return '识别失败'
        out=''
        for r in reply:
            thisnow=correct(r)
            out+=thisnow+' '
        # reply=getEn2(reply)
        # return out
        return '纠错后的结果为：'+out
    if (res<=7.9 and res>=6.0) or res==11 or res==12:
        # last=-1
        print('图片操作集')
        reply=image_allkindsofchange('', '', '', content, res)
        if reply==-1:
            return '请先上传图片'
        if reply[0]=='e':
            return reply[1:]
        return 'c'+reply
    return str(res)

@app.route('/upload', methods=['POST'])
def upload():
    print('start')
    file = request.files['file']
    # 处理上传的文件
    random_int = random.randint(1, 100000)
    print(random_int)

    file.save(f'C://Users//Administrator//Desktop//sys//server//static//pic//'+(str)(random_int)+'.png')
    print(file)
    print(file.filename)
    print('end')
    return str(random_int)

if __name__ == '__main__':
    # last=-1
    init()
    app.run()