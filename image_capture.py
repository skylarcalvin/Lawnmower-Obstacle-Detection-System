import cv2
from os import mkdir
from os.path import expanduser, isdir, getsize

# get home dir of currently logged in user and form directory for images.
imagePath = expanduser('~') + '/Pictures/test/'


# Create video capture object.
video = cv2.VideoCapture(0)

def imageCapture (file):
    
    # Capture videm frame and write it to the file.
    ret, frame = video.read()
    cv2.imwrite(file, frame)


# Initial iterator for the image name.
n = 1

while(getsize(expanduser('~/Pictures')) < 10000):

    # Form image name.
    imageName = imagePath + 'image' + str(n) + '.jpg'

    # Test if ~/Pictures/test/ directory exists.
    # If so run the image capture function.
    if isdir(imagePath):
        
        imageCapture(imageName)

    # If not create the directory and run the image capture function.
    else:

        mkdir(imagePath)

        imageCapture(imageName)

    # Advance the next filename by 1.
    n += 1

# Turn off video capture.
video.release()
cv2.destroyAllWindows()