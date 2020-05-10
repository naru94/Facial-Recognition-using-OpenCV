import numpy as np
import cv2

# open the default camera
cap = cv2.VideoCapture(0)

while(True):
	
	# get a new frame from camera
	# returns two values - ret, frame
	# ret == true if (frame != 0)
	ret, frame = cap.read()
	print(ret)
	
	# To check whether we can read the video filename or the camera
	if(ret == True):
	
		# resize the video frame to reduce the number of pixels
		frame = cv2.resize(frame, (0,0), fx=1,fy=1)
		
		# show the frame
		cv2.imshow("Frame",frame)
		
		# wait for 1 milli-sec
		ch = cv2.waitKey(500)
		# To choose a good value to wait for the next frame, using a camera access is calculated from the speed of the camera. 
		# For example, if a camera works at 20 FPS, a great wait value is 50 = 1000/20.
		
		# if key 'q' is pressed close the video 
		if ch & 0xFF == ord('q'):
			break
	
	# camera is not connected properly or video file is corrupted
	else:
		print("Check if camera is connected properly")
		break

# release the camera or video cap
cap.release()
# It is very important to release all the resources that we use in a Computer Vision application; if we do not do it, we can consume all the RAM memory. 
# We can release the matrices with the release function.

# destroy all windows
cv2.destroyAllWindows()
