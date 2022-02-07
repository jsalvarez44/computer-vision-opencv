import cv2
import numpy as np

img = cv2.imread('10.jpg',1)
# 3. FILTRO GAUSSIANO
gausiano = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('Imagen Original',img)
cv2.imshow('Suavizado - Gaussiano',gausiano)

cv2.waitKey(0)
cv2.destroyAllWindows()
