import cv2
import numpy as np


num_down = 2       # number of downsampling steps
num_bilateral = 8  # number of bilateral filtering steps
#Creamos el objetto de video
#captura = cv2.VideoCapture("video.mp4")
captura = cv2.VideoCapture(0)
 
while True:
     
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        
 
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break
        img_rgb = imagen
        img_color = img_rgb

        for _ in xrange(num_down):
            img_color = cv2.pyrDown(img_color)
         
        
        for _ in xrange(num_bilateral):
            img_color = cv2.bilateralFilter(img_color, d=9,
                                            sigmaColor=9,
                                            sigmaSpace=7)
         
        # upsample image to original size
        for _ in xrange(num_down):
            img_color = cv2.pyrUp(img_color)

        # convert to grayscale and apply median blur
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.medianBlur(img_gray, 7)

        # detect and enhance edges
        img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                         cv2.ADAPTIVE_THRESH_MEAN_C,
                                         cv2.THRESH_BINARY,
                                         blockSize=9,
                                         C=2)

        # convert back to color, bit-AND with color image
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
        height, width = img_edge.shape[:2]
        img_color = cv2.resize(img_color,(width,height))
        img_cartoon = cv2.bitwise_and(img_color, img_edge)

        cv2.imshow("cartoon", img_cartoon)


        
        
        
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

