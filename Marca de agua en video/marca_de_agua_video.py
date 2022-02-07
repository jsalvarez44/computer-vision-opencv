import cv2
import numpy as np

captura = cv2.VideoCapture(0)
logo = cv2.imread('21.png', 1)
h_logo, w_logo, c_logo = logo.shape
cv2.namedWindow('Web Cam')
cv2.moveWindow('Web Cam', 100, 100)
while True:
    lectura, imagen = captura.read()
    if not lectura:

        break
    h, w, c = imagen.shape
    roi_1 = imagen[0:h_logo, 0:w_logo]
    roi_2 = logo
    suma = cv2.addWeighted(roi_1, 0.6, roi_2, 0.4, 0)
    imagen[0:h_logo, 0:w_logo] = suma

    cv2.imshow('Web Cam', imagen)
    tecla = cv2.waitKey(25)

    if tecla == 27:
        break

captura.release()
cv2.destroyAllWindows()
