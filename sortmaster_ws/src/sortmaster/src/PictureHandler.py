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
i = 0
class PictureNode:
    def __init__(self):
        rospy.init_node('picturehandler', anonymous=True)
        rospy.Subscriber("robotdone", String, self.callback)
        self.pub = rospy.Publisher('sortmaster', String, queue_size=10)

        self.Run()

        rospy.spin()


    def get_from_webcam(self):
        """
        Fetches an image from the webcam
        """
        print "try fetch from webcam..."
        stream = urllib.urlopen('http://192.168.0.20/image/jpeg.cgi')
        bytes = ''
        bytes += stream.read(64500)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')

        if a != -1 and b != -1:
            jpg = bytes[a:b + 2]
            bytes = bytes[b + 2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
            return i
        else:
            print "did not receive image, try increasing the buffer size in line 13:"


    def get_coordinates_from_image(self):

        image = cv2.imread('picture.jpg')

        color = TR.FindBrickColor(image)
        print color
        field = TR.FindField(image)

        pixelCoords = PC.get_pixel_coords(image, color)

        realCoords = CC.pixel_2_coordinates(pixelCoords)

        print realCoords[0]
        print realCoords[1]

        x = str(realCoords[0])
        y = str(realCoords[1])
        stringField = str(field)
        toRobot = x + "," + y + "," + stringField

        rospy.loginfo(toRobot)
        self.pub.publish(toRobot)


    def callback(self, data):
        raw_input("Please press a key to continue")
        self.Run()

    def Run(self):
        global i
        if(i < 1):
            raw_input("Please press a key to continue")
            i = 2
        image = self.get_from_webcam()
        cv2.imwrite("picture.jpg", image)
        self.get_coordinates_from_image()



if __name__ == '__main__':
    node = PictureNode()





