# Raspberry PI Obstacle detection System

#### Setup

Create a virtual environment for Python3 and install the requirement packages using requirements.txt

Use Flask to run the app and capture images.

#### Information
image_capture.py contains the code for controlling the usb webcam and capturing images. It will wutomatically shut off when the size if the captured image folder reaches 10 GB.

flaskApp.py contains code for running the image capture script when the flask application starts. Note there is no port that this application runs on. It's sole purpose is to run the image capture function.

#### Progress
At this stge I am working on getting the Raspberry Pi set up to be able to caapture image data. Later on I will begin working on processing that data. The goal is to use a Convolutional Neural Network to build a classification model that can detect if there is an obstacle in front of the mower.


