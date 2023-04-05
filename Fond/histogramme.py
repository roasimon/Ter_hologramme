import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('resized.png')

# Convert the image from BGR to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Extract the saturation channel
saturation = hsv_img[:, :, 1]

# Create a histogram of the saturation values
hist, bins = np.histogram(saturation.ravel(), 256, [0, 256])

# Plot the histogram
plt.hist(saturation.ravel(), 256, [0, 256])
plt.xlabel('Saturation')
plt.ylabel('Frequency')
plt.show()



# Extract the value channel
value = hsv_img[:, :, 2]

# Calculate the total number of pixels in the image
num_pixels = value.shape[0] * value.shape[1]

# Create a histogram of the value values normalized by the number of pixels
hist, bins = np.histogram(value.ravel(), 256, [0, 256], density=True)

# Plot the histogram
plt.hist(value.ravel(), 256, [0, 256], density=True)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

