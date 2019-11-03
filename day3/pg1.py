import cv2
import numpy as np


def processing(img,n):
	img2 = img*n
	cv2.imshow("img_"+(str)(n),img2)



img1 = cv2.imread("img1.jpg",0)

img1 = cv2.resize(img1,(900,900))
for i in range(900):
	for j in range(900):
		st = img1[i][j]
		l = (int)(st/32)
		l = l*32
		u = l+32
		mid = (int)(l/2 + u/2)
		img1[i][j] = l
cv2.imshow("img",img1)
for i in range(1,9):
	img = img1
	processing(img,i)
cv2.imshow("img_sp",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()