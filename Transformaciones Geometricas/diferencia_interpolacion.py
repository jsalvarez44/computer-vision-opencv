import cv2
import numpy as np
img = cv2.imread('cafe.jpg',1)

img_resize_1 = cv2.resize(img,(80,80),
                        interpolation = cv2.INTER_AREA)

img_resize_2 = cv2.resize(img,(80,80),
                        interpolation = cv2.INTER_LINEAR)
img_resize_3 = cv2.resize(img,(80,80),
                        interpolation = cv2.INTER_CUBIC)
print (img.shape)

#cv2.imwrite('imagen escalada.jpg',img_resize)
cv2.imshow('Imagen Original',img)
cv2.imshow('INTER_AREA',img_resize_1)
cv2.imshow('INTER_LINEAR',img_resize_2)
cv2.imshow('INTER_CUBIC',img_resize_3)
cv2.imwrite('inter AREA.jpg',img_resize_1)
cv2.imwrite('inter LINEAR.jpg',img_resize_2)
cv2.imwrite('inter CUBIC.jpg',img_resize_3)
cv2.waitKey(0)
cv2.destroyAllWindows()
