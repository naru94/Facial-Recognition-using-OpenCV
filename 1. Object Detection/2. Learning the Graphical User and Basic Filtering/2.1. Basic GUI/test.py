import numpy as np
import cv2

# read images
lena = cv2.imread("lena.png")

i=0
# create windows
cv2.namedWindow("LenaWindow" + str(i),cv2.WINDOW_NORMAL)

# move window
cv2.moveWindow("LenaWindow" + str(i), 10+(20*i), 10+(20*i));
	
# show images
cv2.imshow("LenaWindows" + str(i), lena)


# wait key function
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows();
