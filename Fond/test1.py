import cv2
import numpy as np

# Charger l'image
img = cv2.imread('resized.png')

# Convertir l'image de BGR à HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Extraire le canal de saturation (S)
s = hsv[:,:,1]

# Appliquer une opération de seuillage pour trouver les pixels ayant une saturation élevée
threshold_value = 150
s_thresholded = cv2.threshold(s, threshold_value, 255, cv2.THRESH_BINARY)[1]

# Afficher l'image originale et l'image seuillée
cv2.imshow('Image originale', img)
cv2.imshow('Pixels saturés', s_thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()

hist = cv2.calcHist([s], [0], None, [256], [0, 256])
cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
threshold = 200

mask = cv2.threshold(s,threshold, 255, cv2.THRESH_BINARY)[1]
saturated_pixels = cv2.bitwise_and(img, img, mask=mask)


cv2.imshow('Ima', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()