import cv2
import numpy as np

# METODOS DE CONVERSION
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print (flags)

img = cv2.imread('1.jpg',1)
escala_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('Escala de Grises',escala_grises)
cv2.imshow('Espacio de color HSV',img_HSV)

cv2.waitKey(0)
cv2.destroyAllWindows()
