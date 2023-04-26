import cv2
import numpy as np
import json

# Charger l'image
img = cv2.imread('origin_images/image_500.jpg')

# Charger les points de référence depuis le fichier JSON
with open('Json/image_500.json') as f:
    data = json.load(f)

# Extraire les points de référence
points = data['points']

# Convertir les points en format NumPy array
pts1 = np.float32(points)

# Définir les dimensions de l'image redimensionnée
width, height = 700, 600
# utiliser des pourcentages
# Définir les points correspondants dans l'image redimensionnée
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Obtenir la matrice de transformation
M = cv2.getPerspectiveTransform(pts1, pts2)

# Appliquer la transformation
res = cv2.warpPerspective(img, M, (width, height))

# Afficher l'image originale et l'image redimensionnée
cv2.imshow('Original', img)
cv2.imshow('Transformation', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('resized_image/image500.jpg',res)
