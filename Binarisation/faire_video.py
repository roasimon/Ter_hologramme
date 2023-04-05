import cv2
import numpy as np
import os

# Chemin vers le dossier contenant les images à binariser
img_folder = "warped_images"

# Liste des noms de fichiers d'images dans le dossier
img_files = os.listdir(img_folder)
output_dir = "binariser"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Binarisation de chaque image

for img_file in img_files:
    img = cv2.imread(os.path.join(img_folder, img_file))
    resized_img = cv2.resize(img, (800, 600))
    hsv_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
    v = hsv_img[:,:,2]
    _, binary_img = cv2.threshold(v, 238, 255, cv2.THRESH_BINARY)
  
    output_path = os.path.join(output_dir,img_file)
    cv2.imwrite(output_path, binary_img)


# Résolution de la vidéo
frame_width = 640
frame_height = 480

# Fréquence d'images de la vidéo
fps = 5

# Codecs disponibles sur votre système (voir la documentation OpenCV pour la liste complète)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Chemin vers le dossier contenant les images
img_folder = "binariser"

# Nom du fichier vidéo à créer
video_name = "result.mp4"

# Obtenir la liste des noms de fichiers d'images dans le dossier
img_files = sorted(os.listdir(img_folder))

# Initialiser le fichier vidéo
out = cv2.VideoWriter(video_name, fourcc, fps, (frame_width, frame_height))

# Boucle pour écrire chaque image dans le fichier vidéo
for img_file in img_files:
    # Lire l'image
    img_path = os.path.join(img_folder, img_file)
    img = cv2.imread(img_path)

    # Redimensionner l'image pour correspondre à la résolution de la vidéo
    resized_img = cv2.resize(img, (frame_width, frame_height))

    # Écrire l'image dans le fichier vidéo
    out.write(resized_img)

# Libérer les ressources
out.release()
cv2.destroyAllWindows()
