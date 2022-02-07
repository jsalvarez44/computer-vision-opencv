import cv2
import numpy as np

image = cv2.imread('21_.jpg',1)

# 1. Conversion a Escala de Grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
_,binary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)

# Operaciones morfologicas
mask = cv2.erode(binary,  None, iterations=4)
mask = cv2.dilate(mask, None, iterations=6)

# 4. Encontar contornos
contornos,_ = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for c in contornos:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    k = cv2.waitKey(0)
    cv2.drawContours(image, [c],-1,(0, 0, 255), 2)

cv2.putText(image,"Pelota de tenis", (x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2) 
cv2.imshow("Rectangulo RECTO", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

