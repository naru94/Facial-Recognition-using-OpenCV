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
kernel = np.ones((1,1),'uint8')
imgS_DILATE = cv2.dilate(auxS, kernel, iterations=1)
imgB_DILATE = cv2.dilate(auxB, kernel, iterations=1)

# Binarize image for segment
thres_adapt_auxS = cv2.adaptiveThreshold(imgS_DILATE, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
thres_adapt_auxB = cv2.adaptiveThreshold(imgB_DILATE, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# Show images
cv2.imshow("BackgroundS", auxS)
cv2.imshow("BackgroundB", auxB)
cv2.imshow("ThreshB", thres_adapt_auxS)
cv2.imshow("ThreshS", thres_adapt_auxB)

# Write images
cv2.imwrite("ThreshS.jpg", thres_adapt_auxS)
cv2.imwrite("ThreshB.jpg", thres_adapt_auxB)
	
# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()