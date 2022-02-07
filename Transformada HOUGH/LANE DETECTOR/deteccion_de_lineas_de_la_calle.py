import cv2
import numpy as np

#Creamos el objetto de video
captura = cv2.VideoCapture("2.mp4")

while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break

        #----- CANNY
        lane_image = imagen.copy()
        gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        canny = cv2.Canny(blur,50,150)

        #----- REGION DE INTERES
        height = canny.shape[0]
        width = canny.shape[1]
        #polygon = np.array([ [(0,height),(width,height),(int(width/2),int(height/2))] ])
        polygon = np.array([ [(0,height),(int(width/3),int(2*height/3)),(int(2*width/3),int(2*height/3)),(width,height)] ])
        mask = np.zeros_like(canny)
        cv2.fillPoly(mask,polygon,255)
    
        masked_image = cv2.bitwise_and(canny,mask)
        ROI = masked_image.copy()

        
        cv2.imshow('ROI', masked_image)

        #----- HOUGH
        """
        theta, rho: resolucion en angulo y distancia en espacio Hough
        threshold: minimo numero de puntos para ser considerado como linea
        minLineLength:  Longitud mínima de la línea. Los segmentos de
                        línea más cortos que esto se rechazan.
        maxLineGap :    la distancia máxima permitida entre los segmentos de
                        línea para tratarlos como una sola línea.
        """

        lines = cv2.HoughLinesP(ROI, 2, np.pi/180, 100,
                                minLineLength = 100,maxLineGap = 500)

        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(imagen,(x1,y1),(x2,y2),(0,255,0),2)
        


        #Mostramos imagen  
        cv2.imshow('Video', imagen)
        #Capturamos teclado
        tecla = cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla == 27:
                 break
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()

