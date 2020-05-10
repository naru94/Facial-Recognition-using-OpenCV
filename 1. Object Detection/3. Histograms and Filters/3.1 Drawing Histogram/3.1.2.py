# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import cv2

# read images
lena = cv2.imread("Lena.png")

# create windows
cv2.namedWindow("Lena",cv2.WINDOW_NORMAL)

# move window
cv2.moveWindow("Lena", 10, 10)

# show images
cv2.imshow("Lena", lena)

# split image into its color channels
channels = cv2.split(lena)

# creates a figure
plt.figure()

# with title
plt.title("'Flattened' Color Histogram")

# with xlabel as ---
plt.xlabel("Bins")

# and ylabel as ---
plt.ylabel("# of Pixels")

# loop over the image channels
for i, channel in enumerate(channels):
	# create a histogram for the current channel and concatenate the resulting histograms for each channel
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])

	# plot the histogram
        if (i==0):
                plt.plot(hist, color = "b")
        elif (i==1):
                plt.plot(hist, color = "g")
        elif (i==2):
                plt.plot(hist, color = "r")
		
		# define the length of x-axis
        plt.xlim([0, 256])

# Display plot
plt.show()

# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
