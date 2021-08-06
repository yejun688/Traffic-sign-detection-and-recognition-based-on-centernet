import cv2
import numpy as np
image=np.zeros((400,400,3),np.uint8)

points=np.array([[150,50],[140,140],[200,170]],np.int32)  #多边形的顶点坐标
cv2.polylines(image,[points],True,(255,0,0))  #画任意多边形
'''
参数2 pts：必选参数。表示待绘制多边形的折线数组--多边形的顶点坐标(按顺序)
参数3 isClosed：必选参数。用于设置绘制的折线是否关闭，若设置为True，则从折线的最后一个顶点到其第一个顶点会自动绘制一条线进行闭合。
参数4 color：必选参数。用于设置多边形的颜色
参数5 lineType：可选参数。用于设置线段的类型，可选8（8邻接连接线-默认）、4（4邻接连接线）和cv2.LINE_AA 为抗锯齿
'''
cv2.imshow('image',image)
cv2.waitKey()