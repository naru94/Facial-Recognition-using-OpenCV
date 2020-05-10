import numpy as np
import cv2

# open the default camera
cap = cv2.VideoCapture(0)

# initialize parameters for drawing circle
color = (0,255,0)
line_width = 3
radius = 100
point = (0,0)

# Mouse callback function
# • event - mouse event types
# • x - x cordinate
# • y - y cordinate
# • flags - name it 
# • param - additional variables you can send them via param

def onMouse(event, x, y, flags, param):
	global point, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		print("Pressed",x,y)
		point = (x,y)

# Create window
cv2.namedWindow("Frame")

# Checks if any mouse action is performed
cv2.setMouseCallback("Frame", onMouse)

# To check whether we can read the video filename or the camera
while(True):
	
	# get a new frame from camera
	ret, frame = cap.read()
	
	# resize the video frame to reduce the number of pixels
	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	
	#draw the circle on mouse click
	cv2.circle(frame, point, radius, color, line_width)
	
	# Show image
	cv2.imshow("Frame",frame)
	
	# wait for 1 milli-sec
	ch = cv2.waitKey(1)
	
	# wait app for 'q' key to exit
	if ch & 0xFF == ord('q'):
		break

# release the camera or video cap
cap.release()

# destroy all windows
cv2.destroyAllWindows()