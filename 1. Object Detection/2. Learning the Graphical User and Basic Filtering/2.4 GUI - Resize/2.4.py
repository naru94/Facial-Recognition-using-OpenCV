import numpy as np
import cv2

# Read image
lena = cv2.imread("Lena.png",1)

# Scale
# • 1st - input image
# • 2nd - desired size for the output
# • 3rd - [optional] scale factor along the horizontal axis
# • 4th - [optional] scale factor along the vertical axis

# Do not preserve Aspect Ratio
lena_half = cv2.resize(lena, (0,0), fx=0.5, fy=0.5)

# Preserve Aspect Ratio
lena_stretch = cv2.resize(lena, (300,300))

# Interpolation methods
lena_stretch_near = cv2.resize(lena, (600,600), interpolation=cv2.INTER_NEAREST)
# • INTER_NEAREST – a nearest-neighbor interpolation 
# • INTER_LINEAR – a bilinear interpolation (used by default) 
# • INTER_AREA – resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method. 
# • INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood 
# • INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood

# Show image
cv2.imshow("Lena Half",lena_half)
cv2.imshow("Lena Stretch",lena_stretch)
cv2.imshow("Lena Stretch near",lena_stretch_near)

# Write image
cv2.imwrite("Lena half.jpg",lena_stretch)
cv2.imwrite("Lena Stretch.jpg",lena_stretch)
cv2.imwrite("Lena Stretch near.jpg",lena_stretch_near)

# wait app for a key to exit
cv2.waitKey(0)

# Destroy the windows
cv2.destroyAllWindows();
