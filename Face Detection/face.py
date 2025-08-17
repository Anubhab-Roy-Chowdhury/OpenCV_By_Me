import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('Face Detection\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)  # Start video capture from the webcam
while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        break  # If no frame is captured, exit the loop
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))  # Detect faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a rectangle around the detected face
    cv2.imshow('Face Detection', frame)  # Display the frame with detected faces    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
        break
cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows