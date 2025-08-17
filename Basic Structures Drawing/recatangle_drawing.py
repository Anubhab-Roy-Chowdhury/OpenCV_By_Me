import cv2 
#Image dimensions: 1600x900

image = cv2.imread('Basics/elon-musk-sam-altman.jpg')
if image is not None:
    print("Image loaded successfully.")
    # You can add further processing of the image here
    pt1= (100, 100)
    pt2= (500, 500)
    color = (234, 0, 255)  # Green color in BGR
    thickness = 4
    cv2.rectangle(image, pt1, pt2, color, thickness)
    print("Rectangle drawn successfully.")
    
    cv2.imwrite('Rectangle_drawn_image.jpg', image)
    print("Image with Rectangle saved successfully.")
    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   
else:   
    print("Error: Could not read the image.")