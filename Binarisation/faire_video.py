import cv2
import numpy as np
import os



# Résolution de la vidéo
frame_width = 640
frame_height = 480

# Fréquence d'images de la vidéo
fps = 5

# Codecs disponibles sur votre système (voir la documentation OpenCV pour la liste complète)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Chemin vers le dossier contenant les images
img_folder = "Binarisation/binariser"

# Nom du fichier vidéo à créer
video_name = "Binarisation/result.mp4"

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
