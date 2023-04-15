import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pickle

def getPosWhitePix(image: str) -> np.ndarray:
    img = cv2.imread(image)
    white = [255, 255, 255]

    indices = np.where(np.all(img == white, axis=-1)) # liste des positions des pixels qu'on veut
    indices = np.array(list(zip(indices[0], indices[1])))

    return indices

if __name__ == '__main__':
    sat_pixels_holo = getPosWhitePix("holo_mask_erod.png")
    sat_pixels_non_holo = getPosWhitePix("holo_mask_dilat.png")
    nb_pixel_holo = len(sat_pixels_holo)
    nb_pixel_non_holo = len(sat_pixels_non_holo)
    class_holo = np.zeros((nb_pixel_holo, 94), dtype=int)
    class_non_holo = np.zeros((nb_pixel_non_holo, 94), dtype=int)

    hsvs = []

    for file in os.listdir("warped_resize"):
        img = cv2.imread(os.path.join("warped_resize", file))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv = np.pad(hsv, ((3, 3), (3, 3), (0, 0)))
        hsvs.append(hsv)

    buffer_max_sat = np.zeros(47, dtype=int)
    buffer_max_h = np.zeros(47, dtype=int)
    k = 0
    i = 0

    for h, w in sat_pixels_holo:
        h += 3
        w += 3
        for file in hsvs:
            tuyau = file[h-3:h+4, w-3:w+4] # tuyau temporel 7x7
            tuyau_sat = tuyau.flatten()[1::3] # reduction des dimensions puis sélection des valeurs de saturations
            tuyau_h = tuyau.flatten()[0::3]
            buffer_max_sat[k] = np.max(tuyau_sat)
            buffer_max_h[k] = np.mean(tuyau_h)
            k += 1
        class_holo[i] = np.concatenate((buffer_max_sat, buffer_max_h), axis=None)
        i += 1
        k = 0
    
    j = 0
    for h, w in sat_pixels_non_holo:
        h += 3
        w += 3
        for file in hsvs:
            tuyau = file[h-3:h+4, w-3:w+4] # tuyau temporel 7x7
            tuyau_sat = tuyau.flatten()[1::3] # reduction des dimensions puis sélection des valeurs de saturations
            tuyau_h = tuyau.flatten()[0::3]
            buffer_max_sat[k] = np.max(tuyau_sat)
            buffer_max_h[k] = np.mean(tuyau_h)
            k += 1
        class_non_holo[j] = np.concatenate((buffer_max_sat, buffer_max_h), axis=None)
        j += 1
        k = 0

    random_indices = np.random.choice(class_holo.shape[0], size=800, replace=False)
    class_holo = class_holo[random_indices, :]    
    random_indices = np.random.choice(class_non_holo.shape[0], size=800, replace=False)
    class_non_holo = class_non_holo[random_indices, :]

    # Générer des données de test
    data = np.concatenate([class_holo, class_non_holo])

    # Utiliser t-SNE pour transformer les données en 3 dimensions
    tsne = TSNE(n_components=2, random_state=42)
    data_tsne = tsne.fit_transform(data)

    # Générer les labels pour chaque classe d'objets
    labels = np.hstack([np.zeros(800), np.ones(800)])

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.scatter(data_tsne[labels==0,0], data_tsne[labels==0,1], c='blue', label='Classe holo')
    plt.scatter(data_tsne[labels==1,0], data_tsne[labels==1,1], c='red', label='Classe non holo')
    ax.set_title('Evolution de la saturation et teinte 2D globale')
    ax.legend()
    plt.savefig("Saturation_teinte_globale.png")
    plt.show()
