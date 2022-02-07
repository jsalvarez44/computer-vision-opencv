"""
TEMPLATE MATCHING
"""
import cv2
import numpy as np

#POSICIONAMIENTO DE VENTANAS
cv2.namedWindow('Original')
cv2.namedWindow('Plantilla')
cv2.namedWindow('ROI')
cv2.namedWindow('Seguimiento')
cv2.namedWindow('Resta')

cv2.moveWindow('Original', 0,0)
cv2.moveWindow('Plantilla', 0,500)
cv2.moveWindow('ROI', 200,500)
cv2.moveWindow('Seguimiento', 650,0)
cv2.moveWindow('Resta', 400,500)

img = cv2.imread("original.jpg",1)
img_original = cv2.imread("original.jpg",0)
img_plantilla = cv2.imread("1.jpg",0)
img_3cn = cv2.merge((img_original, img_original, img_original))
img_plantilla3cn = cv2.merge((img_plantilla, img_plantilla, img_plantilla))
cv2.imshow('Original', img)
cv2.imshow('Plantilla', img_plantilla3cn)
cv2.imshow('Seguimiento', img_3cn)

#POSICION INICIAL DEL ROI Y RECTANGULO
xo = 0
x1 = 100
yo = 0
y1 = 100

for x in range(6):
    for y in range(4):
        cv2.waitKey(1000)
        img_3cnCP = img_3cn.copy()
        cv2.rectangle(img_3cnCP,(xo,yo),(x1,y1),(0,255,0),3)
        cv2.imshow('Seguimiento', img_3cnCP)
        ROI = img_3cn[yo:y1,xo:x1]
        cv2.imshow('ROI', ROI)
        #COMPARACION DE PLANTILLA Y ROI
        resta = cv2.absdiff(img_plantilla3cn, ROI)
        cv2.imshow('Resta', resta)
        if np.sum(resta) < 100000:
            img[yo:y1,xo:x1] = img_plantilla3cn
            cv2.rectangle(img,(xo,yo),(x1,y1),(0,0,255),3)
            cv2.imshow('Original', img)
        #INCREMENTOS EN Y
        yo += 100
        y1 += 100
    #INCREMENTOS EN X CON REAJUSTE DE POSICION EN Y
    yo = 0
    y1 = 100
    x1 += 100
    xo += 100
cv2.imshow('Seguimiento', img_3cn)
cv2.waitKey(0)        
cv2.destroyAllWindows()
