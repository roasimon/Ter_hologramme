import numpy as np
import cv2



im = cv2.imread('resultat.png')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# Appliquer un flou gaussien avec un noyau de 5x5 et un écart type de 0
blur = cv2.GaussianBlur(gray, (9, 9), 0)

edges = cv2.Canny(blur, 60, 150, apertureSize=3)
img = im.copy()
lines = cv2.HoughLines(edges,1,np.pi/180,100)
ymin = ymax = None  # Initialize variables to keep track of min/max y-coordinates
xmin = xmax = None  # Initialize variables to keep track of min/max y-coordinates
for line in lines:
    for rho, theta in line:
        # Check if the line is horizontal (theta is close to 0 or pi)
        if abs(theta) < np.pi/4 or abs(theta - np.pi) < np.pi/4:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 3000 * (-b))
            y1 = int(y0 + 3000 * (a))
            x2 = int(x0 - 3000 * (-b))
            y2 = int(y0 - 3000 * (a))
            # Check if the line is the first or last horizontal line
            if xmin is None or y1 < xmin:
                xmin = y1
                xmin_line = (x1, y1, x2, y2)
                
            if xmax is None or y1 > xmax:
                xmax = y1
                xmax_line = (x1, y1, x2, y2)
            
        elif abs(theta - np.pi/2) < np.pi/4 or abs(theta - 3*np.pi/2) < np.pi/4:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 3000 * (-b))
            y1 = int(y0 + 3000 * (a))
            x2 = int(x0 - 3000 * (-b))
            y2 = int(y0 - 3000 * (a))
            # Check if the line is the first or last horizontal line
            if ymin is None or y1 < ymin:
                ymin = y1
                ymin_line = (x1, y1, x2, y2)
            if ymax is None or y1 > ymax:
                ymax = y1
                ymax_line = (x1, y1, x2, y2)
            
            

# Draw the first and last horizontal lines in red
cv2.line(img, (xmin_line[0], xmin_line[1]), (xmin_line[2], xmin_line[3]), (255, 0, 0), 2)
cv2.line(img, (xmax_line[0], xmax_line[1]), (xmax_line[2], xmax_line[3]), (255, 0, 0), 2)

# Draw the first and last horizontal lines in red
cv2.line(img, (ymin_line[0], ymin_line[1]), (ymin_line[2], ymin_line[3]), (0, 0, 255), 2)
cv2.line(img, (ymax_line[0], ymax_line[1]), (ymax_line[2], ymax_line[3]), (0, 0, 255), 2)

points = []
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        line1 = lines[i][0]
        line2 = lines[j][0]
        rho1, theta1 = line1
        rho2, theta2 = line2
        if abs(theta1 - theta2) < 0.1:  # Check if the lines are parallel
            continue
        A = np.array([[np.cos(theta1), np.sin(theta1)], [np.cos(theta2), np.sin(theta2)]])
        b = np.array([rho1, rho2])
        x0, y0 = np.linalg.solve(A, b)
        x0, y0 = int(np.round(x0)), int(np.round(y0))
        points.append((x0, y0))

for point in points:
    cv2.circle(img, point, 5, (0, 0, 0), -1)
    

# Display the cropped image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

src = np.float32([ [92, 12] ,[420, 12], [63, 343],[447, 350]])
dst = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])

# Calculate the perspective transformation matrix
M = cv2.getPerspectiveTransform(src, dst)

# Apply the perspective transformation to the image
cropped_img = cv2.warpPerspective(im, M, (500, 500))

# Display the cropped image
cv2.imshow('Cropped Image', cropped_img)
cv2.imwrite("resized.png", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()