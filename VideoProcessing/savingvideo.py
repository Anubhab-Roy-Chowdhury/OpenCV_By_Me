import cv2
camera = cv2.VideoCapture(0)  # Open the default camera
# width and height getter fnction
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))   
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) 
recorder = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width, frame_height))
print(f"Camera resolution: {frame_width}x{frame_height}")

while True:
    ret, frame = camera.read()  # Capture a frame
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
camera.release()
cv2.destroyAllWindows()
# Ensure the camera is released and all windows are closed
print("Camera released and all windows closed.")
# # Save the video
# recorder.write(frame)