# Kütüphane Kurulumları

import cv2

video = cv2.VideoCapture(0) # Webcam açma işlemi
#Eğer .mp4 bir videoyu oynatmak istiyorsanız 0 yerine video.mp4 yazın.

while(True):
    deger,frame= video.read() 
    # değer: Video okundaysa 1 değeri döndürür.
    # deger diye değişken yerine alt çizgi(_) kullanariz.
    # _,frame = video.read() gibi :) 
    cv2.imshow("webcam",frame)
    kapat = cv2.waitKey(1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video.release()   
cv2.destroyAllWindows()
