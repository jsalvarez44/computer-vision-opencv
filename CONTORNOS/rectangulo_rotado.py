import cv2
import numpy as np

img = cv2.imread('21_.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,binary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
# Operaciones morfologicas
mask = cv2.erode(binary,  None, iterations=4)
mask = cv2.dilate(mask, None, iterations=6)

# Buscamos contorno en la imagen
contornos,_ = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


# CALCULO DE AREA
for c in contornos:
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    print (box)
    cv2.drawContours(img,[box],0,(0,255,0),2)
    k = cv2.waitKey(0)
    cv2.drawContours(img, [c],-1,(0, 0, 255), 2) 
    cv2.imshow("Rectangulo ROTADO", img)
   
cv2.imwrite('rectangulo Rotado.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

