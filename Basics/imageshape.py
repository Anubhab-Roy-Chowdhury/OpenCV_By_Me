import cv2
img = cv2.imread('Basics\elon-musk-sam-altman.jpg')
if img is not None:
    (h, w) = img.shape[:2]
    print(f"Image dimensions: {w}x{h}")
else:
    print("Error: Could not read the image.")