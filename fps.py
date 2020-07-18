import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)

print(cv2.CAP_PROP_FPS)

prevTime = 0

while True:
    retval, frame = cap.read()
    if not retval:
        break
    curTime = time.time()
    sec = curTime - prevTime
    prevTime = curTime

    fps = 1/(sec)

    str = "FPS : %0.1f" % fps

    cv2.putText(frame, str, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if (key == 27):
        break

cap.release()
cv2.destroyAllWindows()