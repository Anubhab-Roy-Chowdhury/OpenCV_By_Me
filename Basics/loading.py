import cv2 

image = cv2.imread('elon-musk-sam-altman.jpg')
if image is None:
    print("Error: Could not read the image.")
else:
    print("Image loaded successfully.")
   