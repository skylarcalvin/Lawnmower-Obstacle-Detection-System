import cv2
from os import mkdir
from os.path import expanduser, isdir, getsize
from time import sleep

# get home dir of currently logged in user and form directory for images.
imagePath = expanduser('~') + '/Pictures/test/'


# Create video capture object.
video = cv2.VideoCapture(0)

# Functions
def imageCapture (file):
    """
    Function captures the image from video feed and saves it to the passed file.
    """
    
    # Capture videm frame and write it to the file.
    ret, frame = video.read()
    cv2.imwrite(file, frame)



def saveImage(i = 10000000000):
    """
    Function checks if the file directory exists and then envokes and then creates
        it if not before envoking the imageCapture function. It will terminate when
        the image folder reaches 10 GB of storge.
    """

    # Initial iterator for the image name.
    n = 1

    while(getsize(expanduser('~/Pictures')) < i):

        # Form image name.
        imageName = imagePath + 'image' + str(n) + '.jpg'

        # Test if ~/Pictures/test/ directory exists.
        # If so run the image capture function.
        if isdir(imagePath):
            
            imageCapture(imageName)

            # Wait 5 Seconds before advancing to the next iteration.
            sleep(5)

        # If not create the directory and run the image capture function.
        else:

            mkdir(imagePath)

            imageCapture(imageName)

            # Wait 5 Seconds before advancing to the next iteration.
            sleep(5)

        # Advance the next filename by 1.
        n += 1

    # Turn off video capture.
    video.release()
    cv2.destroyAllWindows()