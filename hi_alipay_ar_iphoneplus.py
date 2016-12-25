#!/usr/bin/env python
# -*- coding=utf8 -*-

'''
Author:V
Date:20161224
Function:支付宝推出了AR红包，发红包者会发送一张被均匀黑条挡住的照片，领红包者对着同样的东西扫一扫就行了，这个python将黑条挡住的照片进行修复还原。
'''

import cv2
import numpy as np
import sys

def repair_picture(image_path):    
    image = cv2.imread(image_path)
    
    #定义mask线条粗细，推荐设定为11。
    size = 11
    if image is None:
        print('Failed to load image file.')
        sys.exit(1)
    sp = image.shape
    print sp
    
    mask = np.zeros(image.shape[:2], np.uint8)    
    #定位mask 27条线，此处这么处理是因为有时候图片处理结束了，结果支付宝实在扫不成功可以针对某一条针对性的调整。
    cv2.line(mask,(360,1182),(880,1182),255,size)
    cv2.line(mask,(360,1201),(880,1201),255,size)
    cv2.line(mask,(360,1219),(880,1219),255,size)
    cv2.line(mask,(360,1236),(880,1236),255,size)
    cv2.line(mask,(360,1254),(880,1254),255,size)
    cv2.line(mask,(360,1273),(880,1273),255,size)
    cv2.line(mask,(360,1291),(880,1291),255,size)
    cv2.line(mask,(360,1309),(880,1309),255,size)
    cv2.line(mask,(360,1328),(880,1328),255,size)
    cv2.line(mask,(360,1346),(880,1346),255,size)
    cv2.line(mask,(360,1364),(880,1364),255,size)    
    cv2.line(mask,(360,1382),(880,1382),255,size)
    cv2.line(mask,(360,1400),(880,1400),255,size)
    cv2.line(mask,(360,1418),(880,1418),255,size)
    cv2.line(mask,(360,1437),(880,1437),255,size)
    cv2.line(mask,(360,1455),(880,1455),255,size)
    cv2.line(mask,(360,1473),(880,1473),255,size)
    cv2.line(mask,(360,1491),(880,1491),255,size)
    cv2.line(mask,(360,1509),(880,1509),255,size)
    cv2.line(mask,(360,1527),(880,1527),255,size)
    cv2.line(mask,(360,1546),(880,1546),255,size)
    cv2.line(mask,(360,1565),(880,1565),255,size)
    cv2.line(mask,(360,1583),(880,1583),255,size)
    cv2.line(mask,(360,1601),(880,1601),255,size)
    cv2.line(mask,(360,1619),(880,1619),255,size)
    cv2.line(mask,(360,1637),(880,1637),255,size)
    cv2.line(mask,(360,1655),(880,1655),255,size)
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
    #将手机截屏图片放到这里，此处为iphone7plus截屏，所以图片尺寸高为2208, 宽为1242。
    repair_picture("b.png")
    