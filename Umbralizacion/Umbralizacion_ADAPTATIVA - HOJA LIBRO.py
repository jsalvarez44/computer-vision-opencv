import numpy as np
import cv2


img = cv2.imread ( '7.jpg' , 0)
# Umbralizacion Global
ret, th1 = cv2.threshold (img, 127,255, cv2.THRESH_BINARY)
# Umbralizacion Adaptativa
th2 = cv2.adaptiveThreshold (img, 255,
                             cv2.ADAPTIVE_THRESH_MEAN_C, 
                             cv2.THRESH_BINARY, 15,12)
th3 = cv2.adaptiveThreshold (img, 255,
                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                             cv2.THRESH_BINARY, 21,12)

cv2.imshow('umbral', img)
cv2.imshow('resultado', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()


