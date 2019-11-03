import cv2
import numpy as np
img1 = cv2.imread("img1",0)
img2 = cv2.imread("/home/gyanesha/Desktop/DIP/day2/img2.jpeg",0)
# cv2.imshow("img1",img1)
# cv2.waitKey(0)
# cv2.imshow("img2",img2)
# # cv2.waitKey(0)
img1 = cv2.resize(img1,(640,640))
img2 = cv2.resize(img2,(640,640))
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
for i in range(640):
	for j in range(640):
		img1[i][j] = (int)((img1[i][j]/2 + img2[i][j]/2))
cv2.imshow("img3",img1)
cv2.waitKey(0)

cv2.destroyAllWindows()