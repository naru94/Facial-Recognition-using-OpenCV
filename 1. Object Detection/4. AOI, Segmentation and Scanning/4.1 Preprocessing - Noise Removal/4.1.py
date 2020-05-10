import numpy as np
import cv2

# read images
img = cv2.imread("Img.jpg")
patternS = cv2.imread("Pattern.jpg")

# create windows
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.namedWindow("PatternS",cv2.WINDOW_NORMAL)
cv2.namedWindow("NRImage",cv2.WINDOW_NORMAL)
cv2.namedWindow("NRPatternS",cv2.WINDOW_NORMAL)

# Apply median blur
img_noise = cv2.medianBlur(img, 3)
patternS_noise = cv2.medianBlur(patternS, 3)
# • An input image with a 1, 3, or 4 channel image. When the kernel size is greater than 5, the image depth can only be CV_8U
# • An output image,which is the resulting image, that has the same type and depth as that of the input
# • The kernel size that has the aperture size greater than 1 and an odd value. For example, 3, 5, 7

# Show images
cv2.imshow("Image", img)
cv2.imshow("PatternS", patternS)
cv2.imshow("NRImage", img_noise)
cv2.imshow("NRPatternS", patternS_noise)

# Write images
cv2.imwrite("NRImage.jpg", img_noise)
cv2.imwrite("NRPatternS.jpg", patternS_noise)

# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()