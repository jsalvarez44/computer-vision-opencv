import cv2
import numpy as np

img = cv2.imread('2.jpg',1)

# TRASLACION
filas,columnas,canales = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(columnas,filas))
cv2.imshow('Imagen Trasladada',dst)


cv2.waitKey(0)
cv2.destroyAllWindows()
