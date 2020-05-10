import numpy as np
import cv2

# read images
auxS = cv2.imread("BackgroundS.jpg", 0)
auxB = cv2.imread("BackgroundB.jpg", 0)

# create windows
cv2.namedWindow("BackgroundS",cv2.WINDOW_NORMAL)
cv2.namedWindow("BackgroundB",cv2.WINDOW_NORMAL)
cv2.namedWindow("ThreshS",cv2.WINDOW_NORMAL)
cv2.namedWindow("ThreshB",cv2.WINDOW_NORMAL)

# Dilate the edges
kernel = np.ones((3,3),'uint8')
imgS_DILATE = cv2.dilate(auxS, kernel, iterations=1)
imgB_DILATE = cv2.dilate(auxB, kernel, iterations=1)

# Binarize image for segment
ret, thresh_basic_auxS = cv2.threshold(imgS_DILATE,200,255,cv2.THRESH_BINARY_INV)
ret, thresh_basic_auxB = cv2.threshold(imgB_DILATE,200,255,cv2.THRESH_BINARY_INV)

# Show images
cv2.imshow("BackgroundS", auxS)
cv2.imshow("BackgroundB", auxB)
cv2.imshow("ThreshB", thresh_basic_auxS)
cv2.imshow("ThreshS", thresh_basic_auxB)

# Write images
cv2.imwrite("ThreshS.jpg", thresh_basic_auxS)
cv2.imwrite("ThreshB.jpg", thresh_basic_auxB)
	
# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()