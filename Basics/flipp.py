import cv2 
image = cv2.imread('elon-musk-sam-altman.jpg')
if image is not None:
    print("Image loaded successfully.")
    # You can add further processing of the image here
    cv2.imshow('Loaded Image', image)
    flipped = cv2.flip(image, -1)  # Flip horizontally
    print("Image flipped successfully.")
    cv2.imshow('Rotated Image',flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:   
    print("Error: Could not read the image.")