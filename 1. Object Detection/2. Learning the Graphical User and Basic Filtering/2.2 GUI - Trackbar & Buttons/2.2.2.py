import numpy as np
import cv2

# onChange Call-Back function
def onChange_B(x):
    print("Blue Value " + str(x))

def onChange_G(x):
    print("Green Value " + str(x))
	
def onChange_R(x):
    print("Red Value " + str(x))
	
# Create a black image
color = np.zeros((300,512,3), np.uint8)

# Create window
cv2.namedWindow('Color')

# create switch for ON/OFF functionality
switch = '0 : OFF or 1 : ON'

# create a trackbars
cv2.createTrackbar('B', "Color", 0, 255, onChange_B)
cv2.createTrackbar('G', "Color", 0, 255, onChange_G)
cv2.createTrackbar('R', "Color", 0, 255, onChange_R)

while(True):
	# Show image
	cv2.imshow('Color',color)
	
	# wait app for 'q' key to exit
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
	
	# get trackbar value
	b = cv2.getTrackbarPos('B', 'Color')
	g = cv2.getTrackbarPos('G', 'Color')
	r = cv2.getTrackbarPos('R', 'Color')
	
	# update image pixels with the respective values
	color[:] = [b, g, r]

# Destroy the windows
cv2.destroyAllWindows()
