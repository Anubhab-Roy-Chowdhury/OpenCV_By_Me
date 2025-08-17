import cv2 

image = cv2.imread('elon-musk-sam-altman.jpg')
if image is not None:
    print("Image loaded successfully.")
    # You can add further processing of the image here
    cropped = image[50:400, 100:500]  # Example cropping coordinates
    print("Image cropped successfully.")
    cv2.imshow('Loaded Image', image)
    cv2.imshow('Loaded  cropped Image', cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:   
    print("Error: Could not read the image.")