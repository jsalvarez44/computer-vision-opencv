import cv2
import numpy as np

img = cv2.imread('14.png',0)
kernel = np.ones((5,5),np.uint8)
# APERTURA
apertura = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations = 3)
cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen - APERTURA',apertura)

cv2.waitKey(0)
cv2.destroyAllWindows()

