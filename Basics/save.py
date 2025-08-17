import cv2 

image = cv2.imread('elon-musk-sam-altman.jpg')
if image is not None:
    success = cv2.imwrite('output_image.jpg', image)
    if success:
         print("Image saved successfully.")
    else:
        print("Error: Could not save the image.")
else:   
    print("Error: Could not read the image.")