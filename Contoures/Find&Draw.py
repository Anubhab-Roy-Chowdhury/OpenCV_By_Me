import cv2
import numpy as np
img = cv2.imread('Basics\elon-musk-sam-altman.jpg')  # Load an image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
_, thresholded_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)  # Apply binary thresholding
contours, _ = cv2.findContours(thresholded_img, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)  # Find contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)  # Draw contours on the original image
cv2.imshow('Contours', img)  # Display the image with contours  
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows
# Ensure the camera is released and all windows are closed
print("Contours drawn and all windows closed.")
# # Save the video
# recorder.write(frame)
# recorder.release()  # Release the video writer
# cv2.destroyAllWindows()  # Close all OpenCV windows   
# Ensure the camera is released and all windows are closed
print("Video recording completed and all windows closed.")
