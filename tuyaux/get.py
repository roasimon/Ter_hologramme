import cv2 as cv2
import os


if __name__ == '__main__':
    img = cv2.imread("warped_resize/warped_0.png")
    cv2.imshow("hxh,", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
