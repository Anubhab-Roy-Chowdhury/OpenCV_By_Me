import cv2

face_cascade = cv2.CascadeClassifier('Face Detection\haarcascade_frontalcatface.xml')
if face_cascade.empty():
    print("Error: XML file not loaded. Check path.")
    exit()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

cv2.namedWindow('Face Detection')

def nothing(x):
    pass

cv2.createTrackbar('scaleFactor x100', 'Face Detection', 110, 200, nothing)
cv2.createTrackbar('minNeighbors', 'Face Detection', 5, 10, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    scale = max(cv2.getTrackbarPos('scaleFactor x100', 'Face Detection') / 100, 1.01)
    neighbors = max(cv2.getTrackbarPos('minNeighbors', 'Face Detection'), 1)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=scale, minNeighbors=neighbors)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


