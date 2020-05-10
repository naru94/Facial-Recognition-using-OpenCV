import numpy as np
import cv2

# read images
lena = cv2.imread("lena.png")
photo = cv2.imread("photo.png")

# create windows
# namedWindow() function has two parameters: 
# 1st - constant string with the window's name
# 2nd - optional flags
# default flag = cv2.WINDOW_AUTOSIZE

cv2.namedWindow("Lena NORMAL",cv2.WINDOW_NORMAL)
cv2.namedWindow("Lena AUTOSIZE",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Lena RESIZED",cv2.WINDOW_NORMAL)

# • cv2.WINDOW_NORMAL: Allows the user to resize the window
# • cv2.WINDOW_AUTOSIZE: The window size is automatically adjusted to fit the display image and it is not possible to resize the window
## • cv2.WINDOW_OPENGL: This flag enables OpenGL support

# QT has some more flags
# • WINDOW_FREERATIO or WINDOW_KEEPRATIO: If set to WINDOW_FREERATIO, then the image is adjusted with no respect to its ratio. If set to WINDOW_FREERATIO, then the image is adjusted with respect to its ratio.
# • CV_GUI_NORMAL or CV_GUI_EXPANDED: The first flag enables the basic interface without the status bar and toolbar. The second flag enables the most advanced graphical user interface with the status bar and toolbar.
# default flags = cv2.WINDOW_AUTOSIZE | WINDOW_KEEPRATIO |  CV_GUI_EXPANDED

# move window
cv2.moveWindow("Lena NORMAL", 10, 10);
cv2.moveWindow("Lena AUTOSIZE", 222, 10)

#Resize window, only non-autosize
cv2.resizeWindow("Lena RESIZED", 1024, 1024);

# show images
cv2.imshow("Lena NORMAL",lena)
cv2.imshow("Lena AUTOSIZE",lena)
cv2.imshow("Lena RESIZED",lena)

# display statusbar
# cv2.displayStatusBar("Lena NORMAL", "statusBar", 10)


# wait key function
cv2.waitKey(0)

# destroy the windows
cv2.destroyWindow("Lena NORMAL")
cv2.destroyWindow("Lena AUTOSIZE")
cv2.destroyWindow("Lena RESIZED")
