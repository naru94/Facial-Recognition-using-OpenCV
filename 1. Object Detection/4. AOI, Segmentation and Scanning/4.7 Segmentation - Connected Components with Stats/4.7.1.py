import numpy as np
import cv2

# read images
ThreshS = cv2.imread("ThreshS.jpg", 0)
ThreshB = cv2.imread("ThreshB.jpg", 0)

# Get the shape parameters for empty image
height, width = ThreshS.shape[0:2]

# create windows
cv2.namedWindow("ThreshS",cv2.WINDOW_NORMAL)
cv2.namedWindow("ThreshB",cv2.WINDOW_NORMAL)
cv2.namedWindow("ImageS",cv2.WINDOW_NORMAL)
cv2.namedWindow("ImageB",cv2.WINDOW_NORMAL)

# Apply median blur
ThreshS = cv2.bilateralFilter(ThreshS,3,150,150)
ThreshB = cv2.bilateralFilter(ThreshB,3,150,150)

# Erode the edges
kernel = np.ones((3,3),'uint8')
imgS_ERODE = cv2.erode(ThreshS, kernel, iterations=2)
imgB_ERODE = cv2.erode(ThreshB, kernel, iterations=2)

# Connected Components algorithm
retS, labelsS, statsS, centroidS = cv2.connectedComponentsWithStats(imgS_ERODE, connectivity=8)
retB, labelsB, statsB, centroidB = cv2.connectedComponentsWithStats(imgS_ERODE, connectivity=8)

# Get the shape parameters for empty image
heightS, widthS = labelsS.shape[0:2]
heightB, widthB = labelsB.shape[0:2]

if (retS > 2):
	print("Number of Objects: " + str(retS))
	
	# Intialize binary image
	binaryS = np.zeros([heightS,widthS,3],'uint8')

	for row in range(0,heightS):
		for col in range(0, widthS):
			if labelsS[row][col]==1:
				binaryS[row][col]=[255, 0, 0]
			elif labelsS[row][col]==2:
				binaryS[row][col]=[0, 255, 0]
			elif labelsS[row][col]==3:
				binaryS[row][col]=[0, 0, 255]
			elif labelsS[row][col]==4:
				binaryS[row][col]=[255, 255, 0]
			elif labelsS[row][col]==5:
				binaryS[row][col]=[255, 0, 255]
			elif labelsS[row][col]==6:
				binaryS[row][col]=[0, 255, 255]

if (retB > 2):
	print("Number of Objects: " + str(retB))
	
	# Intialize binary image
	binaryB = np.zeros([heightB,widthB,3],'uint8')

	for row in range(0,heightB):
		for col in range(0, widthB):
			if labelsB[row][col]==1:
				binaryB[row][col]=[255, 0, 0]
			elif labelsB[row][col]==2:
				binaryB[row][col]=[0, 255, 0]
			elif labelsB[row][col]==3:
				binaryB[row][col]=[0, 0, 255]
			elif labelsB[row][col]==4:
				binaryB[row][col]=[255, 255, 0]
			elif labelsB[row][col]==5:
				binaryB[row][col]=[255, 0, 255]
			elif labelsB[row][col]==6:
				binaryB[row][col]=[0, 255, 255]

# • Text data that you want to write
# • Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
# • Font type (Check cv2.putText() docs for supported fonts)
# • Font Scale (specifies the size of font)
# • Regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.


if (retS > 2): 
	for i,x in enumerate(centroidS):
		if (i > 0):
			cv2.putText(binaryS, str(statsS[i, cv2.CC_STAT_AREA]), (int(centroidS[i][0]), int(centroidS[i][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 2, cv2.LINE_AA)
			
if (retB > 2):
	for i,x in enumerate(centroidB):
		if (i > 0):
			cv2.putText(binaryB, str(statsB[i, cv2.CC_STAT_AREA]), (int(centroidB[i][0]), int(centroidB[i][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 2, cv2.LINE_AA)
		
		

cv2.imshow("ThreshS", ThreshS)
cv2.imshow("ThreshB", ThreshB)
cv2.imshow("ImageS", binaryS)
cv2.imshow("ImageB", binaryB)

# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
