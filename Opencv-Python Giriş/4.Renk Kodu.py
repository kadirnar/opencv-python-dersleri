import cv2
import numpy as np

video = cv2.VideoCapture(0) #webcam aç

while(True):
        
    _,frame = video.read() #okuma işlemi
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # sarı renk kodu
    lower_yellow = np.array([18,94,50]) 
    upper_yellow = np.array([48,255,255])
    
    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    kapat = cv2.waitKey(1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # q harfine basınca çık
        break
    
video.release()   
cv2.destroyAllWindows()
   
                             