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
        image = image[83:196, 479:618]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.erode(image, kernel, iterations=1)

        cv2.imwrite("removed_noise.png", image)

        result = pytesseract.image_to_string(Image.open("removed_noise.png"), config='-psm 6')

        return result



    def FindField(self, image):
        field = 1
        return field

#image = cv2.imread('test.jpg')

#image = image[67:412,27:635] #[250:357,484:620]            #[83:196, 479:618] brikfarve coords

##cv2.imwrite("testimage.jpg", trimmed_img)

#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#kernel = np.ones((1, 1), np.uint8)
#image = cv2.dilate(image, kernel, iterations=1)
#image = cv2.erode(image, kernel, iterations=1)

##image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

#cv2.imwrite("removed_noise.png", image)

#result = pytesseract.image_to_string(Image.open("removed_noise.png"),config='-psm 6')

#print("I just read this: " + result)




