import cv2

# Charger l'image
img = cv2.imread('Binarisation\warped_images\warped_0.jpg')
# Obtenir la taille de l'image d'origine
height, width, channels = img.shape

# Définir la nouvelle taille souhaitée
new_width = 640
new_height = int(new_width * height / width)

# Redimensionner l'image tout en conservant sa configuration
resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

# Convertir l'image en HSV
hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

# Diviser l'image en ses canaux de couleur HSV
h, s, v = cv2.split(hsv_img)

# Sélectionner le canal de la saturation
saturation = s

# Appliquer un seuillage sur le canal de la saturation
_, threshold = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Binariser l'image
binary_img = cv2.bitwise_and(resized_img, resized_img, mask=threshold)

# Afficher l'image binarisée
cv2.imshow('Binarised Image', binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()








"""
# Binarisation de chaque image
bin_imgs = []
for img_file in img_files:
    height, width, channels = img_file.shape
    new_width = 640
    new_height = int(new_width * height / width)
    resized_img = cv2.resize(img_file, (new_width, new_height), interpolation=cv2.INTER_AREA)
    hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
    v = hsv_img[:,:,2]
    _, binary_img = cv2.threshold(v, 232, 255, cv2.THRESH_BINARY)

"""