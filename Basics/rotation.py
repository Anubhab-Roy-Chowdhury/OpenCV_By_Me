import cv2 

image = cv2.imread('elon-musk-sam-altman.jpg')
if image is not None:
     print("Image loaded successfully.")
    # You can add further processing of the image here
     cv2.imshow('Loaded Image', image)
     (h,w) = image.shape[:2]
     print(f"Image dimensions: {w}x{h}")
     print("Image dimensions displayed successfully.")
     M  = cv2.getRotationMatrix2D((w/2, h/2),45, 1.0)  # Rotate by 45 degrees
     rotated = cv2.warpAffine(image, M, (w, h))
     cv2.imshow('Rotated Image', rotated)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
else:   
    print("Error: Could not read the image.")