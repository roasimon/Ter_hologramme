import cv2
import numpy as np
img = cv2.imread("test_div_video/image_200.jpg")
# Obtenir la taille de l'image d'origine

height, width, channels = img.shape

# Définir la nouvelle taille souhaitée
new_width = 1000
new_height = int(new_width * height / width)

# Redimensionner l'image tout en conservant sa configuration
resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
# Fonction pour détecter les clics de souris et enregistrer les coordonnées
# Initialiser la liste des points sélectionnés
points = []
def select_points(event, x, y, flags, param):
    # Si un clic de souris est détecté
    if event == cv2.EVENT_LBUTTONDOWN:
        # Enregistrer les coordonnées du clic de souris
        points.append((x, y))
        # Dessiner un cercle sur l'image pour indiquer l'emplacement du clic de souris
        cv2.circle(resized_img, (x, y), 5, (0, 255, 0), -1)
        # Rafraîchir l'affichage de l'image
        cv2.imshow("Image", resized_img)
        # Si quatre points ont été enregistrés, arrêter la détection de clics de souris
        if len(points) == 4:
            cv2.setMouseCallback("Image", lambda *args : None)
            print("Les coordonnées des 4 points sélectionnés sont:")
            print(points)
            
            # Recadrer l'image d'origine en utilisant les coordonnées des quatre points
            pts1 = np.float32([points[0], points[1], points[2], points[3]])
            height, width, channels = img.shape

# Définir la nouvelle taille souhaitée
            new_width = 1000
            new_height = int(new_width * height / width)
            pts2 = np.float32([[0, 0], [new_width, 0], [0, new_height], [new_width, new_height]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(resized_img, matrix, (new_width, new_height))

            # Afficher l'image recadrée
            cv2.imshow("Recadré", result)
            cv2.imwrite("resized.jpg",result)

# Créer une fenêtre pour afficher l'image
cv2.namedWindow("Image")



# Attacher la fonction select_points à la fenêtre pour détecter les clics de souris
cv2.setMouseCallback("Image", select_points)

# Afficher l'image
cv2.imshow("Image", resized_img)
cv2.waitKey(0)


