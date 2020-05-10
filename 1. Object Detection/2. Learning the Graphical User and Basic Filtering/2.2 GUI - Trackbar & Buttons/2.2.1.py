import numpy as np
import cv2

# Create a variable to save the position value in track
pos=1

# onChange Call-Back function
def onChange(pos):
    # Read image
	lena = cv2.imread("Lena.png")

	# Show image
	cv2.imshow("Lena", lena)

	# if trackbar value changes
	if (pos > 0):
        # Apply blur filter
	    lena = cv2.blur(lena,(pos,pos))
	    # Show blurred image
	    cv2.imshow("Lena",lena)


# Create windows
cv2.namedWindow("Lena")

# create a trackbar
lena = cv2.createTrackbar("Blur", "Lena", pos, 15, onChange)

# Call to onChange to init
onChange(pos);

# wait app for a key to exit
cv2.waitKey(0)

# Destroy the windows
cv2.destroyAllWindows();
