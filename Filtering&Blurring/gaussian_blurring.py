import cv2
img = cv2.imread('Basics\elon-musk-sam-altman.jpg')  # Load an image
blurred_img = cv2.GaussianBlur(img, (15, 15), 0)  # Apply Gaussian blur with a kernel size of 15x15
cv2.imshow('Blurred Image', blurred_img)  # Display the blurred image
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows