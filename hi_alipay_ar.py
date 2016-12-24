#!/usr/bin/env python
# -*- coding=utf8 -*-

'''
Author:V
Date:20161223
Function:支付宝推出了AR红包，发红包者会发送一张被均匀黑条挡住的照片，领红包者对着同样的东西扫一扫就行了，这个python将黑条挡住的照片进行修复还原。
'''

import cv2
import numpy as np
import sys

def repair_picture(image_path):    
    image = cv2.imread(image_path)
    
    #定义mask线条粗细，如果是人像，推荐设定为6，如果是物体，推荐设定为7.
    size = 7
    if image is None:
        print('Failed to load image file.')
        sys.exit(1)
    sp = image.shape
    print sp
    
    mask = np.zeros(image.shape[:2], np.uint8)    
    #定位mask 27条线，此处这么处理是因为有时候图片处理结束了，结果支付宝实在扫不成功可以针对某一条针对性的调整。
    cv2.line(mask,(200,649),(550,649),255,size)
    cv2.line(mask,(200,661),(550,661),255,size)
    cv2.line(mask,(200,674),(550,674),255,size)
    cv2.line(mask,(200,687),(550,687),255,size)
    cv2.line(mask,(200,698),(550,698),255,size)
    cv2.line(mask,(200,710),(550,710),255,size)
    cv2.line(mask,(200,722),(550,722),255,size)
    cv2.line(mask,(200,735),(550,735),255,size)
    cv2.line(mask,(200,747),(550,747),255,size)
    cv2.line(mask,(200,759),(550,759),255,size)
    cv2.line(mask,(200,771),(550,771),255,size)
    cv2.line(mask,(200,783),(550,783),255,size)
    cv2.line(mask,(200,795),(550,795),255,size)
    cv2.line(mask,(200,808),(550,808),255,size)
    cv2.line(mask,(200,820),(550,820),255,size)
    cv2.line(mask,(200,832),(550,832),255,size)
    cv2.line(mask,(200,844),(550,844),255,size)
    cv2.line(mask,(200,856),(550,856),255,size)
    cv2.line(mask,(200,868),(550,868),255,size)
    cv2.line(mask,(200,880),(550,880),255,size)
    cv2.line(mask,(200,892),(550,892),255,size)
    cv2.line(mask,(200,905),(550,905),255,size)
    cv2.line(mask,(200,917),(550,917),255,size)
    cv2.line(mask,(200,929),(550,929),255,size)
    cv2.line(mask,(200,941),(550,941),255,size)
    cv2.line(mask,(200,953),(550,953),255,size)
    cv2.line(mask,(200,965),(550,965),255,size)
    #cv2.imshow("TEST", mask)
    #cv2.waitKey(0)    
    
    #修复图片，有两种算法可选cv2.INPAINT_NS和cv2.INPAINT_TELEA，效果其实差不。
    image_repair = cv2.inpaint(image, mask,7,cv2.INPAINT_NS)  
    #image_repair = cv2.inpaint(image, mask,8,cv2.INPAINT_TELEA)
    #cv2.imshow("Inpaint", image_repair)
    
    #输出修复好的图片，命名为"原名称_inpaint.png"，需要自己打开图片使用支付宝扫描抢红包，必要时可以将图片放大再扫。
    cv2.imwrite(str(image_path)[:-4]+'_inpaint.png', image_repair)
    #cv2.waitKey(0)
    #释放窗口    
    cv2.destroyAllWindows() 
    
if __name__ == "__main__":
    #将手机截屏图片放到这里，此处为iphone6s截屏，所以图片尺寸高为1334, 宽为750，如果使用其他手机截屏，需先将图片像素尺寸调整到这个数值上（ps处理或者resize函数）。
    repair_picture("34.png")
    