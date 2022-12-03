# capture video from camera using opencv
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture(0)

# check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    # read the current frame from the webcam
    ret, frame = cap.read()

    # display the current frame
    cv2.imshow('Input', frame)

    # press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# release the VideoCapture object
cap.release()