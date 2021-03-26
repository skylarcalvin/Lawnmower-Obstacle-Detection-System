import cv2

# Create video capture object.
video = cv2.VideoCapture(0)

# Input for while loop.
result = True

# Iterator for the image name.
n = 1

while(result):

    # Form image name.
    imageName = "image" + str(n) + ".jpg"
    
    # Capture videm frame and write it to the file.
    ret, frame = video.read()
    cv2.imwrite("~/Pictures/test/" + imageName, frame)

result = input('Please enter "False" here.')

# Turn off video capture.
video.release()
cv2.destroyAllWindows()