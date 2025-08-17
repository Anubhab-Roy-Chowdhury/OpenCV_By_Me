import cv2
image = cv2.imread('Basics/elon-musk-sam-altman.jpg')
if image is not None:
    print("Image loaded successfully.")
    # You can add further processing of the image here
    pt1= (100, 100)
    pt2= (500, 500)
    color = (234, 0, 255)  # Green color in BGR
    thickness = -1
    cv2.circle(image, (200,400), 50, color, thickness)
    print("Circle  drawn successfully.")
    
    cv2.imwrite('Circle _drawn_image.jpg', image)
    print("Image with circle saved successfully.")
    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   
else:   
    print("Error: Could not read the image.")