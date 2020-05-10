import numpy as np
import cv2

# read images
lena = cv2.imread("Lena.png")

# create windows
cv2.namedWindow("Lena",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Lena Median Filter",cv2.WINDOW_NORMAL)
cv2.namedWindow("Lena Canny Edges",cv2.WINDOW_NORMAL)
cv2.namedWindow("Lena Canny Edges Dilated",cv2.WINDOW_NORMAL)
cv2.namedWindow("Lena Bilateral Filter",cv2.WINDOW_NORMAL)
cv2.namedWindow("Lena Cartoonize",cv2.WINDOW_NORMAL)

# Apply median filter to remove possible noise
lena_MEDIAN=cv2.medianBlur(lena, 7)
# • src − A Mat object representing the source (input image) for this operation
# • dst − A Mat object representing the destination (output image) for this operation
# • ksize − A Size object representing the size of the kernel

# Detect edges with canny
lenaCanny = cv2.Canny(lena_MEDIAN, 70, 100)
# • An input image
# • The first threshold
# • The second threshold
# • The Sobel size aperture
# • The Boolean value to check whether to use a more accurate image gradient magnitude

# Dilate the edges
kernel = np.ones((3,3),'uint8')
lenaCannyd = cv2.dilate(lenaCanny, kernel, iterations=1)

# Scale edges values to 1 and invert values
lenaCannyd= lenaCannyd/255
lenaCannyd= 1-lenaCannyd

# Use float values to allow multiply between 0 and 1
lenaCannyf = np.float32(lenaCannyd)

# Blur the edgest to do smooth effect
lenaCannyf = cv2.blur(lenaCannyf, (5,5))

# Apply bilateral filter to homogenizes color
lenaBF = cv2.bilateralFilter(lena, 5, 150.0, 150.0)
# The bilateral filter parameters are as follows:
# • An input image
# • An output image
# • The diameter of a pixel neighborhood; if it's set to negative, it is computed from a sigma space value
# • A sigma color value
# • A sigma coordinate space

# truncate colors
lenaResult= lenaBF/25
lenaResult= lenaResult*25

# Create a 3 channles for edges
lenaCanny3c = cv2.merge([lenaCannyf,lenaCannyf,lenaCannyf])

# Convert color result to float
lenaResultf = np.float32(lenaResult)

# Multiply color and edges matrices
lenaResultf = cv2.multiply(lenaCanny3c, lenaResultf)

# convert to 8 bits color
lenaResult = np.uint8(lenaResultf)

# Show image
cv2.imshow("Lena", lena)
cv2.imshow("Lena Median Filter", lena_MEDIAN)
cv2.imshow("Lena Canny Edges", lenaCanny)
cv2.imshow("Lena Canny Edges Dilated", lenaCannyd)
cv2.imshow("Lena Bilateral Filter", lenaBF)
cv2.imshow("Lena Cartoonize", lenaResult)

# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
