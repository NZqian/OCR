#-*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import json

def OCR(fileName):
    #from urllib import parse
    URL = "https://webapi.xfyun.cn/v1/service/v1/ocr/general"
    APPID = "5eb7ff89"
    API_KEY = "10f4d76d1d5131d8441673b39af46f97"
    def getHeader():
    #  当前时间戳
        curTime = str(int(time.time()))
    #  支持语言类型和是否开启位置定位(默认否)
        param = {"language": "cn|en", "location": "false"}
        param = json.dumps(param)
        paramBase64 = base64.b64encode(param.encode('utf-8'))

        m2 = hashlib.md5()
        str1 = API_KEY + curTime + str(paramBase64,'utf-8')
        m2.update(str1.encode('utf-8'))
        checkSum = m2.hexdigest()
    # http请求头
        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': APPID,
            'X-CheckSum': checkSum,
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        return header
    # 上传文件并进行base64位编码
    with open(fileName, 'rb') as f:
        f1 = f.read()

    f1_base64 = str(base64.b64encode(f1), 'utf-8')

    data = {
            'image': f1_base64
            }

    r = requests.post(URL, data=data, headers=getHeader())
    result = str(r.content, 'utf-8')
    return json.loads(result)
