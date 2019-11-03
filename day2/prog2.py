import cv2
import numpy as np 

def display_shade(img,n):
	for i in range(640):
		for j in range(640):
			if img[i][j]<n:
				img[i][j] = 0
			else:
				img[i][j] = n
	# img1 = img/n
	st = "img_"+(str)(n)
	cv2.imshow(st,img)

img = cv2.imread("img2.jpeg",0)
cv2.imshow("i1",img)
img2 = cv2.resize(img,(640,640))
cv2.imshow("i2",img2)
# cv2.waitKey(0)
k = 128
for i in range(8):
	display_shade(img2,k)
	k = k/2
# for i in range(640):
# 	for j in range(640):
# 		img2[i][j] = (int)(img2[i][j]/2)

# cv2.imshow("i3",img2)
cv2.waitKey(0)