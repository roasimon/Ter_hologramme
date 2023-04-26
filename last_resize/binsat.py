import cv2

# Charger l'image
image = cv2.imread('Ter_hologramme\last_resize\sat_ecart_type.png')
img_normalized = cv2.normalize(image,image, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

# Afficher l'image binarisée
cv2.imshow('Image binarisée',img_normalized)
cv2.waitKey(0)
cv2.destroyAllWindows()