import numpy as np
import cv2


img = cv2.imread ( '30.jpg' , 0)
img = cv2.medianBlur (img, 5)
ret, th1 = cv2.threshold (img, 127,255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold (img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
            cv2.THRESH_BINARY, 11,2)
th3 = cv2.adaptiveThreshold (img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 11,2)

cv2.imshow('umbral', img)
cv2.imshow('resultado', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()


