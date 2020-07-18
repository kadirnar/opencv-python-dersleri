# Kütüphane Kurulumları
# Türk okuyucular daha iyi anlaması için tüm değişkenler,türkçe yazılmıştır.
# Türkçe değişken kullanmanızı tavsiye etmem. Global değişkenler kullanın.

import cv2

resim = cv2.imread("cember.jpg") # Resmi okuma işlemi
gri_resim = cv2.imread("cember.jpg",0) # Resmi grileştirme işlemi

cv2.imshow("resimler",gri_resim) # Resmi ekranda gösterme işlemi

cv2.waitKey(0) # Pencere kapatma işlemi.
cv2.destroyAllWindows()

