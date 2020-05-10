# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import cv2

# read images
lena = cv2.imread("Lena.png")

# create windows
cv2.namedWindow("Lena",cv2.WINDOW_NORMAL)
cv2.namedWindow("Gray",cv2.WINDOW_NORMAL)

# move window
cv2.moveWindow("Lena", 10, 10);
cv2.moveWindow("Gray", 10, 232);

# convert the image to grayscale and create a histogram
gray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)

# show images
cv2.imshow("Lena", lena)
cv2.imshow("Gray", gray)

# computing a histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# • images: This is the image that we want to compute a histogram for. Wrap it as a list: [myImage]
# • channels: A list of indexes, where we specify the index of the channel we want to compute a histogram for.
# To compute a histogram of a grayscale image, the list would be [0]. To compute a histogram for all three red, green, and blue channels, the channels list would be [0, 1, 2]
# • mask: I am not covering masking, but essentially, a mask is a uint8  image with the same shape as our original image, where pixels with a value of zero are ignored and pixels with a value greater than zero are included in the histogram computation. Using masks allow us to only compute a histogram for a particular region of an image. For now, we’ll just use a value of None for the mask
# • histSize: This is the number of bins we want to use when computing a histogram
# • ranges: The range of possible pixel values. Normally, this is [0, 256] for each channel, but if you are using a color space other than RGB (such as HSV), the ranges might be different

# creates a figure
plt.figure()

# with title
plt.title("Grayscale Histogram")

# with xlabel as ---
plt.xlabel("Bins")

# and ylabel as ---
plt.ylabel("# of Pixels")

# plots the hist
plt.plot(hist)

# xlim
plt.xlim([0, 256])

# displays the plot
plt.show()

# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
