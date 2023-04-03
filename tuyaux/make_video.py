import cv2
import os
import glob

width = 0
height = 0

alpha = 0.7
beta = 1.0 - alpha
mask = cv2.imread("dataset\\templates\hologram_masks\passport_hologram_mask.png") # image du mask de l'hologramme
height, width, _ = mask.shape

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'MJPG'), 2, (width, height))
for filename in glob.glob('C:/Users/melvy/Documents/Prog_VSCode/Python/holoproject/warped_images/*.jpg'):
    img = cv2.imread(filename)
    dst = cv2.addWeighted(img, alpha, mask, beta, 0.0)
    out.write(dst)

out.release()
cv2.destroyAllWindows() 
