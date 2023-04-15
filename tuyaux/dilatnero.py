import cv2
import numpy as np

def erod_mask(img: str):
    mask = cv2.imread(img)
    kernel = np.ones((7, 7), np.uint8)

    img_erosion = cv2.erode(mask, kernel, iterations=1)

    cv2.imshow('Erosion', img_erosion)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("holo_mask_erod.png", img_erosion)

def dilat_mask(img: str):
    mask = cv2.imread(img)
    kernel = np.ones((13, 13), np.uint8)

    img_dilate = cv2.dilate(mask, kernel, iterations=1)
    img_dilate = cv2.bitwise_not(img_dilate, img_dilate, mask=None)

    cv2.imshow('Dilatation', img_dilate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("holo_mask_dilat.png", img_dilate)
