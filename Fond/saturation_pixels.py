import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
img1 = cv2.imread('warped_40.jpg')
# Obtenir la taille de l'image d'origine
height, width, channels = img1.shape

# Définir la nouvelle taille souhaitée
new_width = 640
new_height = int(new_width * height / width)

# Redimensionner l'image tout en conservant sa configuration
img = cv2.resize(img1, (new_width, new_height), interpolation=cv2.INTER_AREA)

# Get the number of pixels in the image
num_pixels = img.shape[0] * img.shape[1]

# Convert the image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lst_coords_ijs = []
#rouge
haut_color = np.array([0, 0, 255]) 
#bleu
bas_color=np.array([255,0,0])
# Print the saturation values 
for i in range(len(hsv_img)):
     for j in range(0,len(hsv_img[i])):
        if (hsv_img[i, j][1] > 125):
           #np.std() est une fonction de la bibliothèque NumPy qui permet de calculer l'écart type d'un tableau multidimensionnel NumPy. Cette fonction prend en entrée un tableau multidimensionnel (comme une image) 
            lst_coords_ijs.append((i, j, hsv_img[i, j][1],(np.std(hsv_img[i,j]))))
            img[i,j]= haut_color
        else:
            img[i,j]= bas_color
            
#(x,y,saturation,ecart-type)
#print(lst_coords_ijs)

cv2.imshow('Image modifiée', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



    
