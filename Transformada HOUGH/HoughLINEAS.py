import cv2
import numpy as np
import math

imagen = cv2.imread('26.png',1)
img = imagen.copy()
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gris = cv2.blur(gris, (3,3))
bordes = cv2.Canny(gris,80,100)
print (imagen.shape)
lines = cv2.HoughLines(bordes,2,np.pi/90,100)#90,50
if lines is not None:
            print (len(lines))
            for line in lines:
                rho,theta = line[0]
                angulo = math.degrees(theta)
                print ("distancia: ",rho)
                print ("Angulo (rad): ",theta)
                print ("Angulo (grados): ",angulo)
                
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
                
                cv2.imshow('LINEAS',img)
                cv2.waitKey(0)
    
cv2.imshow('Imagen Original',imagen)
cv2.imshow('LINEAS',img)
cv2.imshow('BORDES',bordes)


cv2.waitKey(0)
cv2.destroyAllWindows()
