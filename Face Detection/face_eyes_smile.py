import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier(r'Face Detection\haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(r'Face Detection\haarcascade_smile.xml')
eyes_cascade = cv2.CascadeClassifier(r'Face Detection\haarcascade_eye.xml')
cap = cv2.VideoCapture(0)  # Start video capture from the webcam
while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        break  # If no frame is captured, exit the loop
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))  # Detect faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a rectangle around the detected face
        cv2.putText(frame, "Face Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # Draw a rectangle around the detected eyes
        cv2.putText(roi_color, "Eyes Detected", (ex, ey - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)  # Draw a rectangle around the detected smiles
        cv2.putText(roi_color, "Smile Detected", (sx, sy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
   

    cv2.imshow('Face Detection', frame)  # Display the frame with detected faces    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
        break 
if len(faces) == 0:
    print("No face detected")
else:
    print("Face detected")  

if len(eyes) == 0:
    print("No eyes detected")
else:
    print("Eyes detected")  

if len(smiles) == 0:
    print("No smile detected")
else:
    print("Smile detected")   
cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows