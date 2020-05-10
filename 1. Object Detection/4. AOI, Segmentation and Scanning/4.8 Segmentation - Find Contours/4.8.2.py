import numpy as np
import cv2

# Intialize count
countS = 0
countB = 0

# read images
ThreshS = cv2.imread("ThreshS.jpg", 0)
ThreshB = cv2.imread("ThreshB.jpg", 0)

# Apply median blur
ThreshS = cv2.bilateralFilter(ThreshS,3,150,150)
ThreshB = cv2.bilateralFilter(ThreshB,3,150,150)

# Erode the edges
kernel = np.ones((3,3),'uint8')
imgS_ERODE = cv2.erode(ThreshS, kernel, iterations=1)
imgB_ERODE = cv2.erode(ThreshB, kernel, iterations=1)

# Find Contours
contoursS, hierarchyS = cv2.findContours(imgS_ERODE, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoursB, hierarchyB = cv2.findContours(imgB_ERODE, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imgS_ERODE, contoursS, -1, (0,255,0), 3)
cv2.drawContours(imgB_ERODE, contoursB, -1, (0,255,0), 3)

# Get the shape parameters for empty image
heightS, widthS = ThreshS.shape[0:2]
heightB, widthB = ThreshB.shape[0:2]

ThreshSCopy = np.zeros([heightS,widthS,3],'uint8')
ThreshBCopy = np.zeros([heightB,widthB,3],'uint8')

# Intialize parameters
indexS = -1
thicknessS = -1

indexB = -1
thicknessB = - 1

for cS in contoursS:
	if (cv2.contourArea(cS) > 25):
		
		# Initalize color
		# colorS = list(np.random.choice(range(256)))
		colorS = (255,255,0)
		
		# Count
		countS =countS+1
		
		# Draw contours
		cv2.drawContours(ThreshSCopy, [cS], -1, colorS, -1)
	
		# Calculate Area
		areaS = cv2.contourArea(cS)
	
		# Calculate perimeter
		perimeterS = cv2.arcLength(cS, True)
		# True - the points is a closed loop
	
		# Calculate Moments
		MS = cv2.moments(cS)
		cxS = int( MS['m10']/MS['m00'])
		cyS = int( MS['m01']/MS['m00'])
		cv2.circle(ThreshSCopy, (cxS,cyS), 4, (0,0,255), -1)
		
		cv2.putText(ThreshSCopy,"Area:"+str(areaS),(cxS,cyS), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 1, cv2.LINE_AA)
		
for cB in contoursB:
	if (cv2.contourArea(cB) > 25):
		
		# Initalize color
		# colorB = list(np.random.choice(range(256)))
		colorB = (255,255,0)
		
		# Count
		countB =countB+1
		
		# Draw contours
		cv2.drawContours(ThreshBCopy, [cB], -1, colorB, -1)
	
		# Calculate Area
		areaB = cv2.contourArea(cB)
	
		# Calculate perimeter
		perimeterB = cv2.arcLength(cB, True)
		# True - the points is a closed loop
	
		# Calculate Moments
		MB = cv2.moments(cB)
		cxB = int( MB['m10']/MB['m00'])
		cyB = int( MB['m01']/MB['m00'])
		cv2.circle(ThreshBCopy, (cxB,cyB), 4, (0,0,255), -1)
		
		cv2.putText(ThreshBCopy,"Area:"+str(areaB),(cxB,cyB), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 1, cv2.LINE_AA)

# Print count
print("Number of Objects: " + str(countS))
print("Number of Objects: " + str(countB))

# Show image
cv2.imshow("ContoursS", ThreshSCopy)
cv2.imshow("ContoursB", ThreshBCopy)
cv2.imshow("ContoursOutlineS", imgS_ERODE)
cv2.imshow("ContoursOutlineB", imgB_ERODE)
# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
