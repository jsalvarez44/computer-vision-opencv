import cv2
import numpy as np

img = cv2.imread('11.jpg',1)

# 4. FILTRO BILATERAL
bilateral = cv2.bilateralFilter(img,15,75,75)
cv2.imshow('Imagen Original',img)
cv2.imshow('Suavizado - Bilateral',bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
