import cv2
import numpy as np

img = cv2.imread('18.jpg',0)

_,thresh = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
cv2.imshow("Original",img)
kernel = np.ones((5,5),np.uint8)
# DILATACION
dilatacion = cv2.dilate(thresh,kernel,iterations = 5)

cv2.imshow('Imagen Umbralizada',thresh)
cv2.imshow('Imagen Dilatada',dilatacion)
cv2.waitKey(0)
cv2.destroyAllWindows()




