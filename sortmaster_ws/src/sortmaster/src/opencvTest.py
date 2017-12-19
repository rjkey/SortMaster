#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cv2
import cv2.cv as cv
import numpy as np
import sys

image = cv2.imread('picture.jpg')
output = image.copy()

boundaries = [
	#([0,50,50],[10,255,255]),
	([110,50,50],[120,255,255])

]

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(hsv, lower, upper)
	colorOutput = cv2.bitwise_and(image, image, mask = mask)

	# show the images
	#cv2.imshow('image',image)
    	#cv2.imshow('mask',mask)
    	#cv2.imshow('color', colorOutput)
	
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

gray = cv2.cvtColor(colorOutput, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1, 80, param1=120,param2=6, minRadius=16, maxRadius=22)

if circles is not None:

	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
		x = i[0]
		y = i[1]
		r = i[2]

		print x
		print y
		print r
	
     		#draw the outer circle
    		cv2.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
     		#draw the center of the circle
    		cv2.circle(output,(i[0],i[1]),2,(0,0,255),3)

		print("Done!")
		cv2.imshow("Found stuff", output)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
else:
	print("Could not find any circles")



