import numpy as np
import cv2

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
# • Contours: This is the contours output where each detected contour is a vector of points.
# • Hierarchy: This is the optional output vector where we store the hierarchy of contours. This is the topology of the image where we can get the relations between each contour.
# • Image: This is the input binary image.
# • Mode: This is the method used to retrieve the contours:
# 		°° RETR_EXTERNAL: This retrieves only the external contours.
# 		°° RETR_LIST: This retrieves all the contours without establishing the hierarchy.
# 		°° RETR_CCOMP: This retrieves all the contours with two levels of hierarchy: external and holes. If another object is inside one hole, then this is put on the top of the hierarchy.
# °° RETR_TREE: This retrieves all the contours that create a full hierarchy between contours.
# • Method: This allows you to perform the approximation method to retrieve the contours' shapes:
# 		°° CV_CHAIN_APPROX_NONE: This does not apply any approximation to the contours and stores all the contours points.
# 		°° CV_CHAIN_APPROX_SIMPLE: This compresses all the horizontal, vertical, and diagonal segments that store only the start and end points.
# 		°° CV_CHAIN_APPROX_TC89_L1,CV_CHAIN_APPROX_TC89_KCOS This applies the Teh-Chin chain approximation algorithm.
# • Offset: This is the optional point value used to shift all the contours. This is very useful when we work in a ROI and is required to retrieve the global positions.

# Get the shape parameters for empty image
heightS, widthS = ThreshS.shape[0:2]
heightB, widthB = ThreshB.shape[0:2]

ThreshSCopy = np.zeros([heightS,widthS,3],'uint8')
ThreshBCopy = np.zeros([heightB,widthB,3],'uint8')

# Intialize parameters
indexS = -1
thicknessS = -1
colorS = (255, 255, 0)

indexB = -1
thicknessB = - 1
colorB = (255, 255, 0)

# Draw the Contours
cv2.drawContours(ThreshSCopy, contoursS, indexS, colorS)
cv2.drawContours(ThreshBCopy, contoursB, indexB, colorB, thicknessB)
# • Image: This is the output image used to draw the contours.
# • Contours: This is the vector of contours.
# • Contour index: This is a number that indicates the contour to be drawn; if it is negative, all the contours are drawn.
# • Color: This is the color used to draw the contour.
# • Thickness: If this is negative, then the contour is filled with the color chosen.
# • Line type: This is used when we want draw with antialiasing, or other drawing methods.
# • Hierarchy: This is an optional parameter and is only needed if you want to draw only some of the contours.
# • Max level: This is an optional parameter and taken into account only when the hierarchy parameter is available. If it is set to 0, only the specified contour is drawn, and if it is set to 1, the function draws the current contour and the nested as well. If it is set to 2, then the algorithm draws all the specified contour hierarchies.
# • Offset: This is an optional parameter used to shift the contours.

# Show image
cv2.imshow("ContoursS", ThreshSCopy)
cv2.imshow("ContoursB", ThreshBCopy)

# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
