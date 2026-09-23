from fer import FER
import cv2

# Start webcam
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

# Initialize FER detector
detector = FER(mtcnn=True)

while True:

    # Read webcam frame
    ret, frame = cap.read()

    # Detect emotions
    result = detector.detect_emotions(frame)

    # Loop through all detected faces
    for face in result:

        # Get face coordinates
        x, y, w, h = face["box"]

        # Draw rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        # Get emotions dictionary
        emotions = face["emotions"]

        # Find dominant emotion
        dominant_emotion = max(
            emotions,
            key=emotions.get
        )

        # Display emotion text
        cv2.putText(
            frame,
            dominant_emotion,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

    # Show output window
    cv2.imshow(
        "Emotion Detection",
        frame
    )

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()