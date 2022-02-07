import cv2
import numpy as np

img = cv2.imread('22.png',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,binary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
cv2.imshow('Imagen Original',img)
# Operaciones morfologicas
mask = cv2.erode(binary,  None, iterations=4)
mask = cv2.dilate(mask, None, iterations=6)
cv2.imshow('Imagen Binaria',mask)

# Buscamos contorno en la imagen
contornos,_ = cv2.findContours(mask.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print ("Numero de Contornos: ",len(contornos))

# CALCULO DE AREA
for c in contornos:
    area = cv2.contourArea(c)
    k = cv2.waitKey(0)
    cv2.drawContours(img, [c],-1,(0, 0, 255), 2)
    cv2.imshow("Contornos", img)
    print ("Area de Contorno",area)



cv2.waitKey(0)
cv2.destroyAllWindows()

