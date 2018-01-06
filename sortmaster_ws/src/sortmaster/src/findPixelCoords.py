#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cv2
import cv2.cv as cv
import numpy as np
import sys

class PixelCoords:
    def get_pixel_coords(self, image, color):
        boundaries = []
        output = image.copy()

        print "This color was sent to me " + color

        if color != "BLUE" and color != "RED":
            print "Could not find a color!"
            return null

        if color == "BLUE":
            boundaries = [([110, 50, 50], [120, 255, 255])]
            print "got blue"

        if color == "RED":
            boundaries = [([0,50,50],[10,255,255])]
            print "got red"

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        for (lower, upper) in boundaries:
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")

            # find the colors within the specified boundaries and apply
            # the mask
            mask = cv2.inRange(hsv, lower, upper)
            colorOutput = cv2.bitwise_and(image, image, mask=mask)

        gray = cv2.cvtColor(colorOutput, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1, 80, param1=120, param2=10, minRadius=16, maxRadius=22)

        circleList = []

        if circles is not None:

            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                x = i[0]
                y = i[1]
                r = i[2]

                print x
                print y
                print r

                if x < 170 and x > 36 and y > 286 and y < 404:
                    item = [(x,y)]
                    circleList.append(item)

                # draw the outer circle
                cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle
                cv2.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)

                print("Done!")

        else:
            print("Could not find any circles")

        return circleList


