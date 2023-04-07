import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pickle

def getPosWhitePix(image: str) -> list:
    img = cv2.imread(image)
    white = [255, 255, 255]

    indices = np.where(np.all(img == white, axis=-1)) # liste des positions des pixels qu'on veut
    indices = list(zip(indices[0], indices[1]))

    return indices

sat_pixels_holo = getPosWhitePix("Sat_ecart_type_binaire.jpg")
nb_pixel_holo = len(sat_pixels_holo)
class_holo = np.zeros((nb_pixel_holo*47, 1))
class_non_holo = np.zeros((((519*738)-nb_pixel_holo)*47, 1))
i = 0
j = 0

hsvs = []

for file in os.listdir("warped_resize"):
        img = cv2.imread(os.path.join("warped_resize", file))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsvs.append(hsv)

for x in range(0, 519):
    print(x)
    for y in range(0, 738):
        for file in hsvs:
            if (x, y) in sat_pixels_holo:
                class_holo[i] = file[x][y][1]
                i += 1
            else:
                class_non_holo[j] = hsv[x][y][1]
                j += 1
    
print("hello")

class_holo.reshape((nb_pixel_holo, 47))
class_non_holo.reshape(((519*738)-nb_pixel_holo, 47))

# Générer des données de test
data = np.concatenate([class_holo, class_non_holo])

# Utiliser t-SNE pour transformer les données en 3 dimensions
tsne = TSNE(n_components=3, random_state=42)
data_tsne = tsne.fit_transform(data)

sep = nb_pixel_holo

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data_tsne[:,0][0:sep], data_tsne[:,1][0:sep], data_tsne[:,2][0:sep], c='blue', label='Classe 1')
ax.scatter(data_tsne[:,0][sep:], data_tsne[:,1][sep:], data_tsne[:,2][sep:], c='red', label='Classe 2')
ax.legend()
plt.show()

pickle.dump(fig, open('FigureObject.fig.pickle', 'wb'))

"""# Générer les labels pour chaque classe d'objets
labels = np.hstack([np.zeros(n_samples), np.ones(n_samples)])

# Utiliser t-SNE pour transformer les données en 3 dimensions
tsne = TSNE(n_components=3, random_state=42)
data_tsne = tsne.fit_transform(data)"""

"""# Afficher les données transformées en 3 dimensions
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data_tsne[labels==0,0], data_tsne[labels==0,1], data_tsne[labels==0,2], c='blue', label='Classe 1')
ax.scatter(data_tsne[labels==1,0], data_tsne[labels==1,1], data_tsne[labels==1,2], c='red', label='Classe 2')
ax.legend()
plt.show()"""
