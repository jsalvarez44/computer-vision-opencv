import cv2
import numpy as np

img = cv2.imread('20.png',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,binary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
# Operaciones morfologicas
mask = cv2.erode(binary,  None, iterations=4)
mask = cv2.dilate(mask, None, iterations=6)

# Buscamos contorno en la imagen
contornos,_ = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# CALCULO DE AREA
for c in contornos:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    k = cv2.waitKey(0)
    cv2.drawContours(img, [c],-1,(0, 0, 255), 2)
    cv2.putText(image,"Pelota de tenis", (10,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2) 
    cv2.imshow("Rectangulo RECTO", img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()

