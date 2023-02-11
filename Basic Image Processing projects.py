import cv2
import numpy as np

kernel= np.ones((5,5),np.uint8)
img = cv2.imread("t.png")
cv2.imshow("Original",img)
imggray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale",imggray)
imgblur=cv2.GaussianBlur(img, (7,7),0)
cv2.imshow("Blur",imgblur)



cv2.waitKey(0)