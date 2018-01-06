# -*- coding: utf-8 -*-

import math

d1 = 16.5
a1 = 0
a2 = 17.5
d4 = 20.3

class Calculations:

	#Calculating the coordinates
	def CrustInvKin(self, coordinates):
		xcoord = coordinates[0]
		ycoord = coordinates[1]
		zcoord = coordinates[2]
		q1 = math.atan2(ycoord, xcoord)

		#calculate q2 and q3
		r2 = xcoord **2 + ycoord **2
		s = (zcoord - d1)#*-1
		D = (r2 + (s**2) - (a2**2) - (d4**2))/(2*a2*d4)

		q3 = math.atan2(-math.sqrt(1-(D**2)), D)
		q2 = math.atan2(s, math.sqrt(r2)) - math.atan2(d4*math.sin(q3), a2+d4*math.cos(q3))
		q4 = 0

		q2 = q2 - (math.pi/2)

		coords = [q1, q2, q3, q4]

		print q1
		print q2
		print q3
		print q4

		return coords
	
		

	def pixel_2_coordinates(self, pixelCoords):

		stuff = pixelCoords[0]

		for(x, y) in stuff:

			x = x - 2*x

			y = y - 2*y
			print "X VALUE: " + str(x)
			print "Y VALUE: " + str(y)


			xCoord = (y/8.6)+(394/8.6)
			yCoord = (x/8.6)+(330/8.6)

			XcalVar = 1 - 3.5
			YcalVar = 1 - 2

			xCoord = xCoord + XcalVar
			yCoord = yCoord + YcalVar

			print "REAL X VALUE: " + str(xCoord)
			print "REAL Y VALUE: " + str(yCoord)

			coords=[xCoord, yCoord]

		return coords






#for (x, y) in pixelCoords:
	#xCoord = x
	#yCoord = y


	#print x

	#xRealCoord = (-x/8.6)+(394/8.6)
	#yRealCoord = (-y/8.6)+(330/8.6)

	#print xRealCoord

	#print yRealCoord

	#message = "bais"


