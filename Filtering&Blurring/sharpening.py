import cv2
import numpy as np
img = cv2.imread('Basics\elon-musk-sam-altman.jpg')  # Load an image
sharpened_img = cv2.filter2D(img, -10, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))  # Apply sharpening filter
cv2.imshow('Sharpened Image', sharpened_img)  # Display the sharpened image
cv2.waitKey(0)  # Wait for a key press      
cv2.destroyAllWindows()  # Close all OpenCV windows
# Ensure the camera is released and all windows are closed
print("Sharpening completed and all windows closed.")