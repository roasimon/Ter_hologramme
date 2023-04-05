import cv2

# Charger l'image
img = cv2.imread('warped_images\warped_40.jpg')
# Obtenir la taille de l'image d'origine
height, width, channels = img.shape

# Définir la nouvelle taille souhaitée
new_width = 640
new_height = int(new_width * height / width)

# Redimensionner l'image tout en conservant sa configuration
resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)


# Convertir l'image en HSV
hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

# Extraire la composante V
v = hsv_img[:,:,2]

# Appliquer un seuillage sur la composante V
_, binary_img = cv2.threshold(v, 232, 255, cv2.THRESH_BINARY)

# Afficher l'image binaire
cv2.imshow('Binarized Image', binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
