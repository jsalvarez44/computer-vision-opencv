import numpy as np
import cv2

"""
UMBRALIZACION OTSU
"""
image = cv2.imread('6.jpg')

# Convertimos a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Umbral Optimo
retVal, dst = cv2.threshold(gray, 0, 255,
                    cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print (retVal)
cv2.imshow('umbral', image)
cv2.imshow('resultado', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
