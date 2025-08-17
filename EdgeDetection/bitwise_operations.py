import cv2
import numpy as np

# Create two black images (300x300 pixels)
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

# Draw a white circle on img1 (center at (150,150), radius 100)
cv2.circle(img1, (150, 150), 100, 255, -1)

# Draw a white rectangle on img2 (top-left (100,100), bottom-right (250,250))
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)

# Perform bitwise operations
bitwise_and = cv2.bitwise_and(img1, img2)  # Intersection
bitwise_or = cv2.bitwise_or(img1, img2)     # Union
bitwise_not = cv2.bitwise_not(img1)         # Invert (NOT operation)

# Display all images
cv2.imshow("1 - Circle", img1)
cv2.imshow("2 - Rectangle", img2)
cv2.imshow("3 - AND Operation", bitwise_and)
cv2.imshow("4 - OR Operation", bitwise_or)
cv2.imshow("5 - NOT Operation (Circle)", bitwise_not)

# Wait for key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()