import cv2

# Charger l'image
image = cv2.imread('sat_ecart_type.png',0)

ret, binary_img = cv2.threshold(image, 40, 255, cv2.THRESH_BINARY)

# Afficher l'image binarisée
cv2.imshow('Image binarisée', binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()