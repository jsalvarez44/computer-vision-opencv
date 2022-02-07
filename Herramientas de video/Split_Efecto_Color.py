import cv2
import numpy as np

img = cv2.imread('1.png',1)
h,w = img.shape[0:2]
#print (h,w)
final = np.zeros((2*h, 2*w,3), dtype="uint8")
# Dividimos la imagen en sus canales
b , g , r  =  cv2.split(img)

img_r = img.copy()
img_r[:,:,0] = 0
img_r[:,:,1] = 0
img_r[:,:,2] = r
cv2.imshow("imagen_r",img_r)
cv2.imwrite("rojo.jpg",img_r)
img_b = img.copy()
img_b[:,:,0] = b
img_b[:,:,1] = 0
img_b[:,:,2] = 0
cv2.imshow("imagen_b",img_b)
cv2.imwrite("azul.jpg",img_b)
img_g = img.copy()
img_g[:,:,0] = 0
img_g[:,:,1] = g
img_g[:,:,2] = 0
cv2.imshow("imagen_g",img_g)
cv2.imwrite("verde.jpg",img_g)
final[0:h,0:w]=img
final[0:h,w:2*w]=img_r
final[h:2*h,0:w]=img_g
final[h:2*h,w:2*w]=img_b
cv2.imshow("imagen_f",final)
cv2.imwrite("final.jpg",final)
"""
# Combinamos los 3 canalaes
img1 = cv2.merge((b,g,r))
cv2.imshow('Fusion Canales',img1)

# indexacion con numpy
img[:,:,2] = 0 # asignar
r = img[:,:,2] # acceder
"""
cv2.waitKey(0)
cv2.destroyAllWindows()

