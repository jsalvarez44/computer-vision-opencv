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
contornos,_ = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print ("Numero de Contornos: ",len(contornos))

# CALCULO DE AREA
for c in contornos:
    perimetro= cv2.arcLength(c,True)
    print ("Numero de puntos contorno: ",len(c))
    # aproximacion 1%_0.01
    approx = cv2.approxPolyDP(c,0.05*perimetro,True)
    print ("Numero de puntos Aproximacion de contorno: ",len(approx))
    k = cv2.waitKey(0)
    cv2.drawContours(img, [c],-1,(0, 0, 255), 2)
    cv2.drawContours(img, [approx],-1,(0, 255, 0), 2)
    cv2.imshow("Contornos", img)
   

cv2.waitKey(0)
cv2.destroyAllWindows()

