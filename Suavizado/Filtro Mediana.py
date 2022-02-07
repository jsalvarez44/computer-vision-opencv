import cv2
import numpy as np

img = cv2.imread('10.jpg',1)


# 2. FILTRO MEDIANA
mediana = cv2.medianBlur(img,3)
cv2.imshow('Imagen Original',img)
cv2.imshow('Suavizado - Mediana',mediana)

cv2.waitKey(0)
cv2.destroyAllWindows()

