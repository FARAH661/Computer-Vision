import cv2
import numpy as np

kernel= np.ones((5,5),np.uint8)
img = cv2.imread("t.png")
cv2.imshow("Original",img)
imggray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale",imggray)
imgblur=cv2.GaussianBlur(img, (7,7),0)
cv2.imshow("Blur",imgblur)
imgedge=cv2.Canny(img, 100, 100)
cv2.imshow("Edge",imgedge)
imgDilation=cv2.dilate(imgedge,kernel , iterations=1)
cv2.imshow("Dilated image",imgDilation)
imgerode=cv2.erode(imgDilation,kernel , iterations=1)
cv2.imshow("Eroded image",imgerode)

"""
img = cv2.imread("t.png")
cv2.imshow("Original",img)
#print(img.shape)
#imgresized= cv2.resize(img, (1000,500))
#cv2.imshow("imgresized",imgresized)
#imgcropped= img[0:200,200:500]
#cv2.imshow("imgcropped",imgcropped)

#w,h= 350,450
#pts1= np.float32([[100,200],[200,200],[100,400],[200,400]])
#pts2= np.float32([[0,0],[w,0],[0,h],[w,h]])
#matrix= cv2.getPerspectiveTransform(pts1,pts2)
#imgoutput= cv2.warpPerspective(img, matrix,(w,h))
#cv2.imshow("Output",imgoutput)

imgHor=np.hstack((img,img,img))
cv2.imshow("imgHor",imgHor)
imgVer=np.vstack((img,img,img))
cv2.imshow("imgVer",imgVer)"""


cv2.waitKey(0)