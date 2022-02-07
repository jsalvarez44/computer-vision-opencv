import cv2
import numpy as np

img = cv2.imread('2.jpg',1)

# ROTACION
filas,columnas,canales = img.shape
M = cv2.getRotationMatrix2D((columnas/2,filas/2),180,1)
dst = cv2.warpAffine(img,M,(columnas,filas))
cv2.imshow('Imagen Rotada',dst)


cv2.waitKey(0)
cv2.destroyAllWindows()
