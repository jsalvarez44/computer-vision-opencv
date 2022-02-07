import cv2
import numpy as np

imagen = cv2.imread('23.jpg',1)
img = imagen.copy()
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gris = cv2.blur(gris, (3,3))
bordes = cv2.Canny(gris,80,100)
print (imagen.shape)
minLineLength = 10
maxLineGap = 50
"""
theta, rho: resolucion en angulo y distancia en espacio Hough
threshold: minimo numero de puntos para ser considerado como linea
minLineLength:  Longitud mínima de la línea. Los segmentos de
                línea más cortos que esto se rechazan.
maxLineGap :    la distancia máxima permitida entre los segmentos de
                línea para tratarlos como una sola línea.

NOTA: minLineLength == threshold
"""
lines = cv2.HoughLinesP(bordes,rho = 1,theta = 1*np.pi/180,
                        threshold = 100,maxLineGap = 400) #minLineLength = 50

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        
"""
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
"""
cv2.imshow('Imagen Original',imagen)
cv2.imshow('LINEAS',img)
cv2.imshow('BORDES',bordes)


cv2.waitKey(0)
cv2.destroyAllWindows()
