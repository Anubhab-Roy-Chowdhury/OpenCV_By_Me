import cv2
image = cv2.imread('elon-musk-sam-altman.jpg')
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('grayscale_image.jpg', gray)
else:   
    print("Error: Could not read the image.")