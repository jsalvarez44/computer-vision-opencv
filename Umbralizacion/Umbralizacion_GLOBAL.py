import tkinter as tk
import cv2


image = cv2.imread('21_.jpg')

# Convertimos a escala de grises
root = tk.Tk()

root.mainloop()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh = 40

retVal1, dst1 = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

cv2.imshow('umbral', image)
cv2.imshow('resultado', dst1)


cv2.waitKey(0)
cv2.destroyAllWindows()

