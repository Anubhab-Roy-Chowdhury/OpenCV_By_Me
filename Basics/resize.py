import cv2
# width then height
# always save the file with the same name
img = cv2.imread('elon-musk-sam-altman.jpg')
if img is not None:
    resized = cv2.resize(img, (800, 600))
    cv2.imshow('Resized Image', resized)
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('resized_image.jpg', resized)
    print("Image resized and saved successfully.")

else:
    print("Error: Could not read the image.")