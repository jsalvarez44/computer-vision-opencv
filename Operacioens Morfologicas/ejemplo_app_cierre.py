import cv2
import numpy as np

"""
El objetivo es el CIERRE de agujeros en objetos de primer plano
(Monedas) de imagen umbralizada / Dilatacion-Erosion
"""

img = cv2.imread('21_.jpg',0)

_,thresh = cv2.threshold(img,2000,2000,cv2.THRESH_BINARY_INV)
cv2.imshow('Imagen Umbralizada',thresh)

kernel = np.ones((7,7),np.uint8)
# APERTURA
apertura = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen - APERTURA',apertura)

cv2.waitKey(0)
cv2.destroyAllWindows()

