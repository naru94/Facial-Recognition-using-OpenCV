import numpy as np
import cv2

# read images
lena = cv2.imread("Lena.png")

# create windows
cv2.namedWindow("Lena",cv2.WINDOW_AUTOSIZE)

# Create image for halo dark
ones = np.ones([len(lena[0]),len(lena),3],'float32')
halo = ones*0.3
             
# Create circle
cv2.circle(halo, (int((len(lena[0]))/2), int((len(lena[0]))/2)), int((len(lena[0]))/3), (1,1,1), -1)

halo = cv2.blur(halo, (int((len(lena[0]))/2), int((len(lena[0]))/2)))

cv2.imshow("Halo", halo)


# wait key function
cv2.waitKey(0)

# destroys all windows
cv2.destroyAllWindows()
