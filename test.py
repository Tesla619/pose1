import cv2
import numpy as np

# Load the dictionary and parameters for ArUco markers
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_1000)
aruco_params = cv2.aruco.DetectorParameters()

# Create a video capture object for the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture object
    ret, frame = cap.read()
    
    # Detect the ArUco markers in the frame
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)
    
    # Draw the detected ArUco markers on the frame
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    
    # Display the frame with ArUco markers
    cv2.imshow('Frame', frame)
    
    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
