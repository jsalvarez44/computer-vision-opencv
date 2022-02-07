import cv2
import numpy as np
img = cv2.imread('2.jpg',1)

# Escalar-REDIMENSIONAR
img_resize = cv2.resize(img,(320,240),
                        interpolation = cv2.INTER_LINEAR)

#img_resize = cv2.resize(img,None,fx=0.5, fy=0.5,
                        #interpolation = cv2.INTER_LINEAR)


print (img.shape)
print (img_resize.shape)

cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen Escalada',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
