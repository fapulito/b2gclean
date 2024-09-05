import cv2
import numpy as np
import time
import os
nframes = 500
interval = 0.5
fps=100
cap = cv2.VideoCapture('http://192.168.10.140:81/stream')
print("UNIHIKER TimeLapser")
for i in range(nframes):
    # capture
    ret, img = cap.read()
    # save file
    cv2.imwrite('./photos/img_'+str(i+1000).zfill(4)+'.png', img)
    # wait 5 seconds
    time.sleep(interval)
    print("Photo No : ", +i)
 
# Define the path to the photos folder
photos_path = "photos/"
# Get the list of photo filenames
photos = os.listdir(photos_path)
# Sort the photos by name
photos.sort()
# Create a video writer object
video = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc(*"MJPG"), 100, (1280, 720))
 
# Loop through the photos
for photo in photos:
    # Read the photo as an image
    image = cv2.imread(photos_path + photo)
    # Resize the image to fit the video frame
    image = cv2.resize(image, (1280, 720))
    # Write the image to the video
    video.write(image)
 
# Release the video writer object
video.release()
print("Video Build Completed")