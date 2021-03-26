import cv2

# Create video capture object.
video = cv2.VideoCapture(0)

# Iterator for the image name.
n = 1

while(n <= 100):

    # Form image name.
    imageName = "/home/pi/Pictures/test/image" + str(n) + ".jpg"
    
    # Capture videm frame and write it to the file.
    ret, frame = video.read()
    cv2.imwrite(imageName, frame)

    # Advance the next filename by 1.
    n += 1

# Turn off video capture.
video.release()
cv2.destroyAllWindows()