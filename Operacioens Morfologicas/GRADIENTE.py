import cv2
import numpy as np

img = cv2.imread('13.png',0)
kernel = np.ones((5,5),np.uint8)
gradiente = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen - GRADIENTE',gradiente)

cv2.waitKey(0)
cv2.destroyAllWindows()

