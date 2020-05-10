import numpy as np
import cv2

lena = cv2.imread("Lena.png", 1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(lena, 'LENA', (10,100), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
cv2.imshow("Lena", lena)
