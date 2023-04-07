import cv2
import numpy as np
import os

# Chemin vers le dossier contenant les images à binariser
img_folder = "Fond/test_div_video"

# Liste des noms de fichiers d'images dans le dossier
img_files = os.listdir(img_folder)
output_dir = "Fond/binariser"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)


# Binarisation de chaque image

for img_file in img_files:
    img = cv2.imread(os.path.join(img_folder, img_file))
    height, width, channels = img.shape

# Définir la nouvelle taille souhaitée
    new_width = 600
    new_height = int(new_width * height / width)

# Redimensionner l'image tout en conservant sa configuration
    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
  # Définir les valeurs minimales et maximales pour chaque canal
    h_min, s_min, v_min = 0, 19, 185
    h_max, s_max, v_max = 180, 255, 255
   # Créer un masque binaire pour les pixels qui correspondent aux valeurs définies
    mask = cv2.inRange(hsv_img, (h_min, s_min, v_min), (h_max, s_max, v_max))

# Appliquer le masque à l'image originale pour obtenir l'image binaire
    binary_img = cv2.bitwise_and(resized_img, resized_img, mask=mask)
  
    output_path = os.path.join(output_dir,img_file)
    cv2.imwrite(output_path, binary_img)
