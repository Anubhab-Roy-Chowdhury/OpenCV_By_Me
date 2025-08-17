import cv2
img = cv2.imread('Basics\elon-musk-sam-altman.jpg', cv2.IMREAD_GRAYSCALE)  # Load an image
thres=cv2.threshold(img, 80 ,255, cv2.THRESH_BINARY)  # Apply binary thresholding
cv2.imshow('Thresholded Image', thres[1])  # Display the thresholded image
cv2.waitKey(0)  # Wait for a key press  
cv2.destroyAllWindows()  # Close all OpenCV windows
# Ensure the camera is released and all windows are closed  
print("Thresholding completed and all windows closed.")