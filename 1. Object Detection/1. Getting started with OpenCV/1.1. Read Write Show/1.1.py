# reading and writing images

import numpy as np
import cv2

# read images
color = cv2.imread("img/Lena.png")
#color = cv2.imread("lena.png", 1)
#color = cv2.imread("lena.png", cv2.IMREAD_COLOR)
#print(color.shape)

gray = cv2.imread("img/Lena.png", 0)
#gray = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
print(gray.dtype)

#bit32 = cv2.imread("img/Lena.png", cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
#bit32 = cv2.imread("Lena.png", cv2.IMREAD_UNCHANGED)
#print(bit32.dtype)

# imread() is the main function used to read images. This function opens an image and stores the image in a matrix format
# two parameters -
# 1st - string that contains the image's path
# 2nd - (optional) 
# • cv2.IMREAD_ANYDEPTH: If set to this constant, returns a 16-bit/32-bit image when the input has the corresponding depth; otherwise, the imread function converts it to an 8-bit image
# • cv2.IMREAD_COLOR: If set to this constant, always converts the image to color
# • cv2.IMREAD_GRAYSCALE: If set to this constant, always converts the image to grayscale image and stores the image in a matrix format
# • cv2.IMREAD_UNCHANGED: If set to this constant, reads a Transparent PNG or TIFF in OpenCV


# show images
cv2.imshow("Lena BGR",color)
cv2.imshow("Lena Gray",gray)
#cv2.imshow("Lena 32",bit32)

# wait key function
cv2.waitKey(5)

# write images
cv2.imwrite("color.jpg",color)
cv2.imwrite("gray.jpg",gray)
#cv2.imwrite("bit32.jpg",bit32)
