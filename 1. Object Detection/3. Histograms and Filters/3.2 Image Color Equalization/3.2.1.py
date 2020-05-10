import numpy as np
import cv2

# read images
lena = cv2.imread("Lena.png")

# create windows
cv2.namedWindow("Lena",cv2.WINDOW_NORMAL)
cv2.namedWindow("Lena Equalized",cv2.WINDOW_NORMAL)

# move windows
cv2.moveWindow("Lena", 10, 10)
cv2.moveWindow("Lena Equalized", 10, 222)

# Convert color BGR to YCrCb
lena_YCrCb = cv2.cvtColor(lena, cv2.COLOR_BGR2YCrCb)

# Split image into channels
Y,Cr,Cb = cv2.split(lena_YCrCb)

# Equalize the Y channel only
Y = cv2.equalizeHist(Y)

# Merge the result channels
lena_YCrCb = cv2.merge([Y,Cr,Cb])

# Convert color YCrCb to BGR
lena_EQUALIZED = cv2.cvtColor(lena_YCrCb, cv2.COLOR_YCrCb2BGR)

# show images
cv2.imshow("Lena", lena)
cv2.imshow("Lena Equalized", lena_EQUALIZED)

# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
