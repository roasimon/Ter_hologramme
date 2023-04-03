import os 
import cv2
import numpy as np
from math import floor, ceil

centre_tuyau = (183, 657) # choix plus ou moins au hasard parmi la liste d'indices

def tuyauSaturation(im_dir: str, height: int, width: int, size: int):
    resize_path = os.listdir(im_dir)
    saturations_7 = []
    saturations_non_holo = []
    fl = int(floor(size/2))
    cl = int(ceil(size/2))

    for i in range(len(resize_path)):
        img = cv2.imread(os.path.join("warped_resize", resize_path[i]))

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        tuyau = hsv[height-fl:height+cl, width-fl:width+cl]
        s_max = np.max(tuyau.flatten()[1::3])
        saturations_7.append(s_max)

        tuyau = hsv[81-fl:81+cl, 382-fl:382+cl]
        s_max = np.max(tuyau.flatten()[1::3])
        saturations_non_holo.append(s_max)

    return saturations_7, saturations_non_holo

def tuyauTeinte(im_dir: str, height: int, width: int, size: int):
    resize_path = os.listdir(im_dir)
    teinte_7 = []
    teinte_non_holo = []

    fl = int(floor(size/2))
    cl = int(ceil(size/2))

    for i in range(len(resize_path)):
        img = cv2.imread(os.path.join("warped_resize", resize_path[i]))

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        tuyau = hsv[height-fl:height+cl, width-fl:width+cl]
        s_max = np.mean(tuyau.flatten()[0::3])
        teinte_7.append(s_max)

        tuyau = hsv[81-fl:81+cl, 382-fl:382+cl]
        s_max = np.mean(tuyau.flatten()[0::3])
        teinte_non_holo.append(s_max)

    return teinte_7, teinte_non_holo

def getListPixSat(im_dir: str) -> np.ndarray:
    resize_path = os.listdir(im_dir)
    bin_img_sat = np.full((519, 738), 0, dtype=np.uint8)
    hsvs = []

    for file in resize_path:
        img = cv2.imread(os.path.join(im_dir, file))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv = np.pad(hsv, ((3, 3), (3, 3), (0, 0)))
        hsvs.append(hsv)
    
    kernel_x = 3
    kernel_y0 = 3
    kernel_y = 3

    buffer_maxs_sat = []

    for x in range(0, 519):
        for y in range(0, 738):
            for file in hsvs:
                tuyau = file[kernel_x-3:kernel_x+4, kernel_y-3:kernel_y+4] # tuyau temporel 7x7
                tuyau = tuyau.flatten()[1::3] # reduction des dimensions puis sélection des valeurs de saturations
                buffer_maxs_sat.append(np.max(tuyau))
            bin_img_sat[x][y] = np.std(buffer_maxs_sat)
            kernel_y += 1
            buffer_maxs_sat.clear()
        kernel_x += 1
        kernel_y = kernel_y0
    
    return bin_img_sat

def getListPixTeinte(im_dir: str) -> np.ndarray:
    resize_path = os.listdir(im_dir)
    bin_img_h = np.full((519, 738), 0, dtype=np.uint8)
    hsvs = []

    for file in resize_path:
        img = cv2.imread(os.path.join(im_dir, file))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv = np.pad(hsv, ((3, 3), (3, 3), (0, 0)))
        hsvs.append(hsv)
    
    kernel_x = 3
    kernel_y0 = 3
    kernel_y = 3

    buffer_mean_h = []

    for x in range(0, 519):
        for y in range(0, 738):
            for file in hsvs:
                tuyau = file[kernel_x-3:kernel_x+4, kernel_y-3:kernel_y+4] # tuyau temporel 7x7
                tuyau = tuyau.flatten()[0::3] # reduction des dimensions puis sélection des valeurs de teinte
                buffer_mean_h.append(np.mean(tuyau))
            bin_img_h[x][y] = np.std(buffer_mean_h)
            kernel_y += 1
            buffer_mean_h.clear()
        kernel_x += 1
        kernel_y = kernel_y0
    
    return bin_img_h
