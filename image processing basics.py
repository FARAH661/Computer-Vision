import imutils
import cv2
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("E:\pyimagesearch computer vision\jp.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d));
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
#Accessing individual pixels
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))
#Array slicing and cropping
roi = image[60:160, 20:78]
cv2.imshow("ROI", roi)
#Image resizing
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)  #We use // to perform integer math (i.e., no floating point values).
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)   
cv2.imshow("Imutils Rotation", rotated)
# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, -45)
cv2.imshow("Imutils Bound Rotation", rotated)
# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
#Drawing functions
output = image.copy()
cv2.rectangle(output, (20, 60), (40, 80), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
output = image.copy()
cv2.circle(output, (20, 60), 20, (255, 0, 0), -1) #(img, center, radius, color, thickness)
cv2.imshow("Circle", output)
output = image.copy()
cv2.line(output, (20, 60), (40, 80), (0, 0, 255), 5)
cv2.imshow("Line", output)
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)

