import numpy as np
import cv2

# read images
img = cv2.imread("NRImage.jpg")
patternS = cv2.imread("NRPatternS.jpg")

#img = cv2.resize(img, img.shape[:,:,2], interpolation=cv2.INTER_NEAREST)

# create windows
cv2.namedWindow("PatternS",cv2.WINDOW_NORMAL)
cv2.namedWindow("PatternB",cv2.WINDOW_NORMAL)
cv2.namedWindow("BackgroundS",cv2.WINDOW_NORMAL)
cv2.namedWindow("BackgroundB",cv2.WINDOW_NORMAL)

# Basic and effective way to calculate the light pattern from one image
patternB = cv2.blur(img, (int(len(img[0])/2),int(len(img)/2)))

# Subtract the image by the pattern
auxS = patternS - img
auxB = patternB - img

# Show images	
cv2.imshow("Image", img)
cv2.imshow("PatternS", patternS)
cv2.imshow("PatternB", patternB)
cv2.imshow("BackgroundS", auxS)
cv2.imshow("BackgroundB", auxB)

# Write images
cv2.imwrite("BackgroundS.jpg", auxS)
cv2.imwrite("BackgroundB.jpg", auxB)

# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
