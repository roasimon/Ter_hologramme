import cv2
import numpy as np

# Charger l'image
img = cv2.imread('resultat.png')

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
# Appliquer un filtre de Canny pour détecter les contours
edges = cv2.Canny(blur,60,150,apertureSize = 3)

# Détecter les droites avec la transformée de Hough
lines = cv2.HoughLines(edges,1,np.pi/180,100)

# Calculer la distance entre chaque paire de droites
distances = []
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        rho1, theta1 = lines[i][0]
        rho2, theta2 = lines[j][0]
        a1, b1 = np.cos(theta1), np.sin(theta1)
        a2, b2 = np.cos(theta2), np.sin(theta2)
        x0_1, y0_1 = a1*rho1, b1*rho1
        x0_2, y0_2 = a2*rho2, b2*rho2
        d = np.sqrt((x0_1 - x0_2)**2 + (y0_1 - y0_2)**2)
        distances.append((i, j, d))

# Supprimer les droites dont la distance est inférieure à un seuil
MIN_DISTANCE = 0
indices_to_remove = set()
for i, j, d in distances:
    if d < MIN_DISTANCE:
        indices_to_remove.add(j)
        

# Dessiner les droites restantes
for i, line in enumerate(lines):
    if i not in indices_to_remove:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 3000*(-b))
        y1 = int(y0 + 3000*(a))
        x2 = int(x0 - 3000*(-b))
        y2 = int(y0 - 3000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
       




# Afficher l'image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

