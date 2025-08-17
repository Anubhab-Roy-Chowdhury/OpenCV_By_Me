import cv2
import numpy as np
img = np.zeros((400, 400,3), dtype=np.uint8)
#Draw a triangle
pts = np.array([[100, 300], [200, 100], [300, 300]])
cv2.fillPoly(img, [pts], (255, 255, 255))
img_=np.zeros((400, 400,3), dtype=np.uint8)
#Draw a square
pts = np.array([[50, 50], [150, 50], [150, 150], [50, 150]])
cv2.fillPoly(img_, [pts], (255, 255, 255))
#Draw a rectangle
img1 = np.zeros((400, 400,3), dtype=np.uint8)
pts = np.array([[200, 50], [350, 50], [350, 150], [200, 150]])
cv2.fillPoly(img1, [pts], (255, 255, 255))  
#Draw a pentagon
img2 = np.zeros((400, 400,3), dtype=np.uint8)
pts = np.array([[100, 300], [150, 200], [250, 200], [300, 300], [200, 350]])
cv2.fillPoly(img2, [pts], (255, 255, 255))
#Draw a hexagon
img3 = np.zeros((400, 400,3), dtype=np.uint8)
pts = np.array([[100, 300], [150, 200], [250, 200], [300, 300], [250, 400], [150, 400]])
cv2.fillPoly(img3, [pts], (255, 255, 255))  
#Draw a heptagon
img4 = np.zeros((400, 400,3), dtype=np.uint8)
pts = np.array([[100, 300], [150, 200], [250, 200], [300, 300], [250, 400], [150, 400], [200, 350]])
cv2.fillPoly(img4, [pts], (255, 255, 255))
#Draw an octagon
img5 = np.zeros((400, 400,3), dtype=np.uint8)
pts = np.array([[100, 300], [150, 200], [250, 200], [300, 300], [250, 400], [150, 400], [200, 350], [200, 250]])
cv2.fillPoly(img5, [pts], (255, 255, 255))
#Draw a circle
img__ = np.zeros((400, 400,3), dtype=np.uint8)
cv2.circle(img__, (200, 200), 100, (255, 255, 255), -1)
# # Combine all shapes into one image
# img = cv2.add(img, img_)
# img = cv2.add(img, img1)
# img = cv2.add(img, img2)
# img = cv2.add(img, img3)
# img = cv2.add(img, img4)
# img = cv2.add(img, img5)
# img = cv2.add(img, img6)
# Convert to grayscale  
gray = cv2.cvtColor(img__, cv2.COLOR_BGR2GRAY)
# Detect threshold using threshold_
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw contours on the original image
for contour in contours:
    per= cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.00002 * per, True)
    x, y, w, h = cv2.boundingRect(approx)
    if len(approx) == 3:
        cv2.putText(img__, "Triangle", (x +70, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)    
    elif len(approx) == 4:
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            cv2.putText(img__, "Square", (x +70, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        else:
            cv2.putText(img__, "Rectangle", (x +70, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    elif len(approx) == 5:
        cv2.putText(img__, "Pentagon", (x +70, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    elif len(approx) == 6:
        cv2.putText(img__, "Hexagon", (x +70, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    elif len(approx) == 7:
        cv2.putText(img__, "Heptagon", (x +70, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    elif len(approx) == 8:
        cv2.putText(img__, "Octagon", (x +70, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    else:
        cv2.putText(img__, "Circle", (x +70, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
# Show the image with detected shapes
cv2.imshow("Shapes", img__)
cv2.waitKey(0)
cv2.destroyAllWindows()

