import cv2
import numpy as np

img = cv2.imread('13.png',0)
kernel = np.ones((5,5),np.uint8)
# EROSION
erosion = cv2.erode(img,kernel,iterations = 6)
cv2.imshow('Imagen MASCARA',img)
cv2.imshow('Imagen Erosionada',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()




