import cv2
import numpy as np

mask = cv2.imread("resize_mask.png")
mask = cv2.bitwise_not(mask, mask=None)
kernel = np.ones((4, 4), np.uint8)

img_erosion = cv2.dilate(mask, kernel, iterations=1)

cv2.imshow('Erosion', img_erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("holo_mask_erod.png", img_erosion)
