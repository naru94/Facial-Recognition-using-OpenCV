import numpy as np
import cv2

# read images
auxS = cv2.imread("BackgroundS.jpg", 0)
auxB = cv2.imread("BackgroundB.jpg", 0)

# Get the shape parameters for empty image
height, width = auxS.shape[0:2]

# Intialize binary image
binaryS = np.zeros([height,width,1],'uint8')
binaryB = np.zeros([height,width,1],'uint8')


# create windows
cv2.namedWindow("BackgroundS",cv2.WINDOW_NORMAL)
cv2.namedWindow("BackgroundB",cv2.WINDOW_NORMAL)
cv2.namedWindow("Slow BinaryS",cv2.WINDOW_NORMAL)
cv2.namedWindow("Slow BinaryB",cv2.WINDOW_NORMAL)

# # Dilate the edges
# kernel = np.ones((3,3),'uint8')
# imgS_DILATE = cv2.dilate(auxS, kernel, iterations=1)
# imgB_DILATE = cv2.dilate(auxB, kernel, iterations=1)

for row in range(0,height):
	for col in range(0, width):
		if auxS[row][col]>30 and auxS[row][col]<150:
			binaryS[row][col]=255

for row in range(0,height):
	for col in range(0, width):
		if auxS[row][col]>30 and auxS[row][col]<150:
			binaryB[row][col]=255



# Show images
cv2.imshow("BackgroundS", auxS)
cv2.imshow("BackgroundB", auxB)
cv2.imshow("Slow BinaryS",binaryS)
cv2.imshow("Slow BinaryB",binaryB)

# # Dilate the edges
# kernel = np.ones((1,1),'uint8')
# imgS_DILATE = cv2.dilate(binaryS, kernel, iterations=1)
# imgB_DILATE = cv2.dilate(binaryB, kernel, iterations=1)

# Write images
cv2.imwrite("ThreshS.jpg", binaryS)
cv2.imwrite("ThreshB.jpg", binaryB)
	
# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
