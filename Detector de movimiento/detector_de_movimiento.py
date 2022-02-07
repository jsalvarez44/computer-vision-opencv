import numpy as np
import cv2
import time

camara = cv2.VideoCapture(0)
frame_width = int(camara.get(3))
frame_height = int(camara.get(4))
out = cv2.VideoWriter('salida_0.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                      25, (frame_width, frame_height))

fondo = None

while True:
    (grabbed, frame) = camara.read()

    if not grabbed:
        break

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gris = cv2.GaussianBlur(gris, (7, 7), 0)

    if fondo is None:
        fondo = gris
        continue

    resta = cv2.absdiff(fondo, gris)

    _, umbral = cv2.threshold(resta, 50, 255, cv2.THRESH_BINARY)

    umbral = cv2.erode(umbral,  None, iterations=2)
    umbral = cv2.dilate(umbral, None, iterations=25)

    copia_frame = frame.copy()
    img_fg = cv2.bitwise_and(copia_frame, copia_frame, mask=umbral)

    contornosimg = umbral.copy()

    im, contornos, hierarchy = cv2.findContours(contornosimg, cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)

    for c in contornos:
        area = cv2.contourArea(c)
        if area < 8000:
            continue

        (x, y, w, h) = cv2.boundingRect(c)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (6, 1, 205), 7)
        cv2.drawContours(frame, [c], -1, (0, 0, 255), 1, cv2.LINE_AA)

        roi_1 = copia_frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (159, 173, 33), -1)

        roi = frame[y:y+h, x:x+w]
        dst = cv2.addWeighted(roi, 0.4, roi_1, 0.6, 0)
        frame[y:y+h, x:x+w] = dst

    out.write(frame)

    cv2.imshow("frame", frame)

    cv2.imshow('Deteccion de movimiento', frame)

    key = cv2.waitKey(25) & 0xFF
    if key == 27:
        break


camara.release()
out.release()
cv2.destroyAllWindows()
