import cv2
img = cv2.imread('Basics\elon-musk-sam-altman.jpg', cv2.IMREAD_GRAYSCALE)  # Load an image
edges = cv2.Canny(img, 100, 200)  # Apply Canny edge detection
cv2.imshow('Canny Edges', edges)  # Display the edges
cv2.waitKey(0)  # Wait for a key press  
cv2.destroyAllWindows()  # Close all OpenCV windows