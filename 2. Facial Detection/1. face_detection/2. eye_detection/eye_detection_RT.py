import numpy as np
import cv2

cap = cv2.VideoCapture(0)
path = "haarcascade_eye.xml"
eye_cascade = cv2.CascadeClassifier(path)

while(True):
    ret, frame = cap.read()
    
    eyes = eye_cascade.detectMultiScale(frame, scaleFactor=1.02,minNeighbors=20,minSize=(10,10))

    for (x, y, w, h) in eyes:
        xc = (x + x+w)/2
        yc = (y + y+h)/2
        radius = w/2
        cv2.circle(frame, (int(xc),int(yc)), int(radius), (255,0,0), 2)
    cv2.imshow("Frame",frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
