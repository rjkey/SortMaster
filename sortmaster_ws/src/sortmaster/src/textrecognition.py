#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cv2
import cv2.cv as cv
import numpy as np
import sys
import pytesseract
from PIL import Image
import os

class TextRecognition:


    def FindBrickColor(self, image):
        colorArray = ["BLUE", "RED"]
        image = image[83:196, 479:618]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.erode(image, kernel, iterations=1)

        cv2.imwrite("removed_noise_brick.png", image)

        result = pytesseract.image_to_string(Image.open("removed_noise_brick.png"), config='-psm 6')

        if result in colorArray:
            return result

        else:
            print "Could not find a color"
            return null




    def FindField(self, image):
        colorArray = ["1", "2", "3", "4"]
        image = image[250:357,484:620]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.erode(image, kernel, iterations=1)

        cv2.imwrite("removed_noise_field.png", image)

        result = pytesseract.image_to_string(Image.open("removed_noise_field.png"), config='-psm 6')

        if result in colorArray:
            return result

        else:
            print "Could not find a valid number"
            return null




