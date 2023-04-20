import cv2
import numpy as np
import json
import os

def getMaskPixelsPos(mask_path: str) -> list:
    mask = cv2.imread(mask_path)
    mask = cv2.resize(mask, (500, 500))
    white = [255, 255, 255]

    indices = np.where(np.all(mask == white, axis=-1)) # liste des positions des pixels qu'on veut
    indices = list(zip(indices[0], indices[1]))

    return indices

def changePerspecAllImages(im_dir: str, corners_dir: str, dst_dir: str, psp_type: int) -> None:
    lst_im = os.listdir(im_dir)[:-1] # liste des images
    lst_corners = os.listdir(corners_dir) # liste des corners

    for i in range(len(lst_im)):
        img = cv2.imread(os.path.join(im_dir, lst_im[i])) # on récupère l'image
        with open(os.path.join(corners_dir, lst_corners[i])) as f: # on récupère le fichier json qui contient les corners
            data = json.load(f)["document"]["templates"][f"uto.passport.type{psp_type}:main"]["template_quad"] # on récupère les corners

        src = np.float32(data) # position initial du passeport dans l'image
        dst = np.float32([[0, 0], [4920, 0], [4920, 3463], [0, 3463]]) # nouvelle position du passeport = corners du mask de l'hologramme

        M = cv2.getPerspectiveTransform(src, dst) # création de la transformation de perspective (utile pour le projet image)
        warped = cv2.warpPerspective(img, M, (4920, 3463)) # application de la transformation à l'image avec les nouvelles dimensions
        cv2.imwrite(os.path.join(dst_dir, f"warped_{i}.png"), warped)

def getSaturationFromPixel(im_dir: str, indices: list):
    saturations = [] # liste des valeurs de saturation d'un pixel
    saturations_non_holo = [] # liste des valeurs de saturation d'un pixel

    lst_im = os.listdir(im_dir) # liste des images
    for i in range(len(lst_im)):
        img = cv2.imread(os.path.join(im_dir, lst_im[i])) # on récupère l'image
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # conversion en hsv

        # on met dans la liste la valeur de saturation d'un pixel de l'image en prenant un position aléatoire
        saturations.append(hsv[indices[5][0]][indices[5][1]][1])
        saturations_non_holo.append(hsv[200][200][1])
    
    return (saturations, saturations_non_holo)

def resizeAllImages(im_dir: str, dst_dir: str):
    resize_path = os.listdir(im_dir)

    for i in range(len(resize_path)):
        img =  cv2.imread(os.path.join(im_dir, resize_path[i]))

        height = img.shape[0]
        width = img.shape[1]

        # We want the new image to be 60% of the original image
        scale_factor = 0.15
        new_height = int(height * scale_factor)
        new_width = int(width * scale_factor)
        dimensions = (new_width, new_height)
        new_image = cv2.resize(img, dimensions, interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(os.path.join(dst_dir, f"warped_{i}.png"), new_image)

