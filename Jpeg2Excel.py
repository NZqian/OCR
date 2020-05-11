#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import cv2
import os
import ocr
import json
from sys import argv

def genExcel(infoList, fileName):
    titles = ["序号", "日期", "入厂时间", "出厂时间", "车号", "客户代号",
             "料号", "总重", "空重", "净重"]
    dic = dict(zip(titles, infoList))
    df = pd.DataFrame(columns=titles)
    df.append(dic, ignore_index=True)
    print(df)
    df.to_excel("1.xlsx", index=None)

def compressImage(imageName):
    img = cv2.imread(imageName, 1)
    cv2.imwrite(imageName, img, [cv2.IMWRITE_JPEG_QUALITY, 80])

def main(imageName):
    fsize = os.path.getsize(imageName)
    fsize /= 1024*1024
    print(fsize)
    if fsize > 1. :
        compressImage(imageName)
    imgOCR = ocr.OCR(imageName)
    print(type(imgOCR))
    print(json.dumps(imgOCR, indent=2))
    infoList = []
    for line in imgOCR["data"]["block"][0]["line"]:
        infoList.append(line["word"][0]["content"])
    genExcel(infoList, "1.excel")

if __name__ == "__main__":
    print(argv)
    if len(argv) > 1:
        main(argv[1])
    else:
        main("5.jpg")
    
