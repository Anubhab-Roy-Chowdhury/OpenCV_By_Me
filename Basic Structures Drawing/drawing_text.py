import cv2 
#Image dimensions: 1600x900

image = cv2.imread('Basics/elon-musk-sam-altman.jpg')
if image is not None:
    print("Image loaded successfully.")
    # You can add further processing of the image here
  
    color = (0, 0, 255)  # Green color in BGR
    thickness = 4
    textedimg = cv2.putText(image, 'Hello AI Lovers', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)
    cv2.imshow('Loaded Image', textedimg)
    cv2.imwrite('Text_drawn_image.jpg', image)
    print("Image with Text saved successfully.")
    cv2.imshow('Loaded Image', textedimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
  
   
   
else:   
    print("Error: Could not read the image.")