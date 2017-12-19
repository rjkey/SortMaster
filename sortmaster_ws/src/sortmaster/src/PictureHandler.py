#!/usr/bin/env python
import cv2
import urllib
import numpy as np
import math
from textrecognition import TextRecognition
from findPixelCoords import PixelCoords
from CrustCalculations import Calculations

TR = TextRecognition()
PC = PixelCoords()
CC = Calculations()

import rospy
import time
from std_msgs.msg import String

def get_from_webcam():
    """
    Fetches an image from the webcam
    """
    print "try fetch from webcam..."
    stream=urllib.urlopen('http://192.168.0.20/image/jpeg.cgi')
    bytes=''
    bytes+=stream.read(64500)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')

    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        return i
    else:
        print "did not receive image, try increasing the buffer size in line 13:"

def get_coordinates_from_image():
    pub = rospy.Publisher('sortmaster', String, queue_size=10)
    rospy.init_node('picturehandler', anonymous=True)
    image = cv2.imread('picture.jpg')

    color = TR.FindBrickColor(image)
    print color
    field = TR.FindField(image)
    print field

    pixelCoords = PC.get_pixel_coords(image, color)
    #print pixelCoords[0]
    realCoords = CC.pixel_2_coordinates(pixelCoords)

    #toRobot = [realCoords[0], realCoords[1], field]
    #x = str(realCoords[0])
    #y = str(realCoords[1])
    #stringField = str(field)
    toRobot = "Hello!" #x + "," + y + "," + stringField

    i = 0
    while (i != 4):
        i = i + 1
        rospy.loginfo(toRobot)
        pub.publish(toRobot)
        time.sleep(2)


if __name__ == '__main__':
    image = get_from_webcam()
    cv2.imwrite("picture.jpg", image)
    get_coordinates_from_image()
    #image = cv2.imread('picture.jpg')
    #cv2.imshow('raw',image)



