import cv2

cap = cv2.VideoCapture(0)  # Open the default camera

while True:
    ret, frame = cap.read()  # Capture a frame
    if not ret:
        print("Error: Could not read from the camera.")
        break

    cv2.imshow('Captured Frame', frame)  # Display the captured frame

    # Wait for key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Capture stopped by user.")
        cv2.imwrite('captured_frame.jpg', frame)  # Save the last frame
        break

# Release resources properly
cap.release()
cv2.destroyAllWindows()
# Ensure the camera is released and all windows are closed
print("Camera released and all windows closed.")