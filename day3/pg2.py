import cv2
import numpy as np


def zoom(img,scale):
	x,y = img.shape
	print(x)
	print(y)
	new_x = x*scale
	new_y = y*scale
	new_img=np.zeros(shape=(new_x,new_y), dtype=int)
	new_img = new_img.astype(np.uint8)
	
	for i in range(new_x):
		for j in range(new_y):
			ist = (int)(i/scale)
			jst = (int)(j/scale)
			new_img[i][j] = (img[ist][jst])
	return new_img



def shrink(img,scale):
	x,y = img.shape
	new_x = (int)(x/scale)
	new_y = (int)(y/scale)
	new_img = np.zeros(shape=(new_x,new_y))
	new_img = new_img.astype(np.uint8)
	for i in range(new_x):
		for j in range(new_y):
			ist = (i*scale)
			jst = (j*scale)
			new_img[i][j] = img[ist][jst]
	return new_img


# /home/gyanesha/Desktop/DIP/images/duck.jpg
img1 = cv2.imread("img1.jpg",0)
img1 = cv2.resize(img1,(500,500))
img2 = zoom(img1,2)
img3 = shrink(img1,2)

cv2.imshow("img1",img1)

cv2.imshow("img2",img2)
cv2.imshow("img3",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()