import cv2 

image = cv2.imread('elon-musk-sam-altman.jpg')
if image is not None:
    h,w,c= image.shape
    print(f"Image dimensions\n Height={h}\n Width={w}\n Channels={c}")

else:   
    print("Error: Could not read the image.")