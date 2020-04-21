#!/usr/bin/python3
# -*- encoding:utf-8 *-*

import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('E:\\Visual_code\\tongue_trainer\\xml\\cascade.xml')
img = cv2.imread("C:\\Users\\Keyone\\Desktop\\1020.jpg")
#img = cv2.imread("E:\\company_KeyOne\\舌头数据集3-300\\TongeImageDataset\\dataset\\2.bmp")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.000111,#该参数需要根据自己训练的模型进行调参
        minNeighbors=4,#minNeighbors控制着误检测，默认值为3表明至少有3次重叠检测，我们才认为人脸确实存
        minSize=(20,20),#寻找人脸的最小区域。设置这个参数过大，会以丢失小物体为代价减少计算量。
        flags = cv2.IMREAD_GRAYSCALE
    )
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()