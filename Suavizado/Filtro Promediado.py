import cv2
import numpy as np

img = cv2.imread('10.jpg',1)
# 1. FILTRO PROMEDIADO
promediado = cv2.blur(img,(5,5))
cv2.imshow('Imagen Original',img)
cv2.imshow('Suavizado - Promedio',promediado)

cv2.waitKey(0)
cv2.destroyAllWindows()
