import cv2
import numpy as np

# Create black image and draw a circle (outline instead of filled)
img = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.circle(img, (200, 200), 100, (255, 255, 255), 2)  # Use thickness=2 instead of -1

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur (important for HoughCircles)
#gray = cv2.GaussianBlur(gray, (9, 9), 2)

# Detect circles
circles = cv2.HoughCircles(
    gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
    param1=100, param2=30, minRadius=80, maxRadius=120
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)  # Circle outline
        cv2.circle(img, (x, y), 2, (0, 0, 255), 3)  # Center point
        cv2.putText(img, "Circle", (x - 30, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
else:
    print("No circles were found")

# Show result
cv2.imshow("Circles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()





