import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while cam.isOpened():
    state,frame =cam.read()
    if not state:
        print("could not read from webcam 0")
        break
    
    cv2.imshow("webcam0", frame)
    if cv2.waitkey(1) ==ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break