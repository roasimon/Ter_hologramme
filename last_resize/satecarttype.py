import os 
import cv2
import numpy as np


def getListPixSat(im_dir: str) -> np.ndarray:
    resize_path = os.listdir(im_dir)
    bin_img_sat = np.full((600, 700), 0, dtype=np.uint8)
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
    for x in range(0, 600):
        for y in range(0, 700):
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


im_dir = "Ter_hologramme/last_resize/resized_image"
binary_image = getListPixSat(im_dir)

# Display the binary image
cv2.imshow("sat binaryImage", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('sat_ecart_type.png',binary_image)
