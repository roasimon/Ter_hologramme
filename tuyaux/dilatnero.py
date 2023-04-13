import cv2
import numpy as np

mask = cv2.imread("resize_mask.png")
kernel = np.ones((7, 7), np.uint8)

img_erosion = cv2.erode(mask, kernel, iterations=1)

cv2.imshow('Erosion', img_erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("holo_mask_erod.png", img_erosion)
