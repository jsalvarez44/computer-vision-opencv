import cv2
import numpy as np
import time


#Creamos el objetto de video
captura = cv2.VideoCapture(0)
captura.set(3,640)
captura.set(4,480)
contador = 0
while True:
        if contador == 0:
                start = time.time()
                e1 = cv2.getTickCount()
                
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break
        end = time.time()
        seconds = end - start 
        print ("Time taken : {0} seconds".format(seconds))
        fps  = contador / seconds
        contador = contador + 1
        if contador == 120:
                print ("Estimated frames per second : {0}".format(fps))
                e2 = cv2.getTickCount()
                t = (e2 - e1)/cv2.getTickFrequency()
                fps_2 = contador/t
                print ("opcion_2",fps_2)
                contador = 0
        #Mostramos imagen  
        cv2.imshow('Video', imagen)
        #Capturamos teclado
        tecla = cv2.waitKey(1) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla == 27:
                 break
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()

