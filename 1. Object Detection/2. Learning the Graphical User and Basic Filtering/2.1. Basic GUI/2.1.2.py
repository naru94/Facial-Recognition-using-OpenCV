import numpy as np
import cv2

# read images
lena = cv2.imread("lena.png")

for i in range(10):
	
	windowName = "Lena" +str(i)
	# create windows
	cv2.namedWindow(windowName,cv2.WINDOW_NORMAL)

	# move window
	cv2.moveWindow(windowName, 10+(20*i), 10+(20*i));
	
	# show images
	cv2.imshow(windowName, lena)


# wait key function
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows();