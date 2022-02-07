import cv2
import numpy as np

img = cv2.imread('8.jpg',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retVal,binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

# Buscamos contorno en la imagen
contornos, hierarchy = cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print len(contornos)
cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen Binaria',binary)

# Dibujar Contornos
cnt = contornos[1]
print len(cnt)
for cnt in contornos:
    cv2.drawContours(img, [cnt], -1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("contornos",img)
    cv2.waitKey(0)
    
#cv2.drawContours(img, contornos, -1, (0, 0, 255), 2, cv2.LINE_AA)
#cv2.drawContours(img, [cnt], -1, (0, 0, 255), 2, cv2.LINE_AA)
#cv2.imshow('Contornos',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

