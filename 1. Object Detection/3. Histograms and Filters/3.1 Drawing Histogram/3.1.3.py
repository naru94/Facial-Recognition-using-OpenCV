# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import cv2

# read images
lena = cv2.imread("Lena.png")

# create windows
cv2.namedWindow("Lena",cv2.WINDOW_NORMAL)

# move window
cv2.moveWindow("Lena", 10, 10);

# show images
cv2.imshow("Lena", lena)

# split image into its color channels
chans = cv2.split(lena)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
features = []

# loop over the image channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and
	# concatenate the resulting histograms for each
	# channel
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	features.extend(hist)

	# plot the histogram
	plt.plot(hist, color = color)
	
	# define the length of x-axis
	plt.xlim([0, 256])

# Display plot
plt.show()

# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
