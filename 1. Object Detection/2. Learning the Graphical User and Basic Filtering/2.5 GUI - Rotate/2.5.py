import numpy as np
import cv2

# Read image
lena = cv2.imread("lena.png",1)

# get image height, width
(h, w) = lena.shape[:2]

# Rotation
# C 1st - axis/point of rotation (center)
# • 2nd - angle of rotation
# • 3rd - scale
M = cv2.getRotationMatrix2D((w/2,h/2), -30, 1)

# window to display the image
# • 1st - input image
# • 2nd - output image
# • 3rd - size of window
rotated = cv2.warpAffine(lena, M, (lena.shape[1], lena.shape[0]))

# Show image
cv2.imshow("Rotated",rotated)

# wait app for a key to exit
cv2.waitKey(0)

# Destroy the windows
cv2.destroyAllWindows()
