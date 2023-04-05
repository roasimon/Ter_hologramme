import cv2

# Ouvrir la vidéo
video_capture = cv2.VideoCapture('pass.mp4')

# Initialiser le compteur d'images
count = 0

# Définir la fréquence de capture d'images
frame_rate = 50

# Boucle de capture d'images
while True:
    # Lire une image à partir de la vidéo
    ret, frame = video_capture.read()

    # Si la vidéo est terminée, sortir de la boucle
    if not ret:
        break

    # Capturer une image toutes les 50 trames
    if count % frame_rate == 0:
        cv2.imwrite(f'image_{count}.jpg', frame)

    # Augmenter le compteur d'images
    count += 1

# Fermer la vidéo et terminer le programme
video_capture.release()
cv2.destroyAllWindows()