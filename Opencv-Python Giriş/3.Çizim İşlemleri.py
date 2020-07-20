# Kütüphane Kurumları

import cv2
import numpy as np

img = np.zeros((1280,720,3),np.uint8) # 1280-720 boyutunca 0'lardan oluşan bir siyah resim
cv2.line(img,(0,0),(500,600),(255,255,255),5) # Hat çizimi
cv2.rectangle(img,(0,0),(715,600),(100,150,255),5) #Dikdörtgen çizimi
cv2.circle(img,(550,535),60,(255,23,42),3) #Dikdörtgen çizimi

cv2.imshow("resim",img)


cv2.waitKey(0) # Pencere kapatma işlemi.
cv2.destroyAllWindows()
