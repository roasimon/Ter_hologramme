import cv2
import numpy as np
import matplotlib.pyplot as plt
  
# Reading an image
img = cv2.imread('4.jpg')
# Define the new size
new_width = 500
new_height = 500
new_size = (new_width, new_height)

# Resize the image
raised = cv2.resize(img, new_size)


  
# converting the image to HSV format
hsv = cv2.cvtColor(raised, cv2.COLOR_BGR2HSV)
""""
# Define the range of red color in HSV format
red_lower_hue = np.array([0, 100, 100])
red_upper_hue = np.array([10, 255, 255])
red_lower_hue_2 = np.array([170, 100, 100])
red_upper_hue_2 = np.array([180, 255, 255])

mask_red1 = cv2.inRange(hsv, red_lower_hue, red_upper_hue)
mask_red2 = cv2.inRange(hsv, red_lower_hue_2, red_upper_hue_2)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)
"""

lower= np.array([0, 0, 0])
upper = np.array([180, 255, 30])


mask_noir = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(raised,raised, mask= mask_noir)


# display the mask and masked image

# Inverting the mask 
mask_yellow = cv2.bitwise_not(mask_noir)
Mask = cv2.bitwise_and(raised, raised, mask = mask_yellow)
  
# Displaying the image
cv2.imshow('mask',mask_noir)
cv2.waitKey(0)
# Convert image to image gray
tmp = cv2.cvtColor(Mask, cv2.COLOR_BGR2GRAY)

# Applying thresholding technique
_, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)

# Using cv2.split() to split channels
# of coloured image
b, g, r = cv2.split(Mask)

# Making list of Red, Green, Blue
# Channels and alpha
rgba = [b, g, r, alpha]

# Using cv2.merge() to merge rgba
# into a coloured/multi-channeled image
dst = cv2.merge(rgba, 4)

# Writing and saving to a new image
cv2.imwrite("resultat.png", dst)
cv2.imshow("resultat",dst)
cv2.waitKey(0)
