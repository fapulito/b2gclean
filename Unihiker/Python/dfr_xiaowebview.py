# From Opencv

# import the opencv library
import cv2
# define a video capture object
vid = cv2.VideoCapture(http://192.168.10.140:81/stream)

while(True):
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    resize = cv2.resize(frame, (380, 280))
    cv2.imshow('frame', resize)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()