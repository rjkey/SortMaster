#!/usr/bin/env python
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction
from control_msgs.msg import FollowJointTrajectoryFeedback
from control_msgs.msg import FollowJointTrajectoryResult
from control_msgs.msg import FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from trajectory_msgs.msg import JointTrajectory
import math
from CrustCalculations import Calculations

from std_msgs.msg import String
from std_msgs.msg import Float64

CC = Calculations()

class ActionExampleNode:

	N_JOINTS = 4
	def __init__(self,server_name):
		self.client = actionlib.SimpleActionClient(server_name, FollowJointTrajectoryAction)
		self.joint_positions = []

		self.pub = rospy.Publisher("gripper/command", Float64)
		self.pub.publish(1)

		global roboXCoord
		global roboYCoord
		global roboZCoord

		self.names = ["joint1",
					  "joint2",
					  "joint3",
					  "joint4"
					  ]
		jointPositions = [[roboXCoord, roboYCoord, roboZCoord, 0], [0,0,0,0]]

		dur = rospy.Duration(1)

		for p in jointPositions:
			jtp = JointTrajectoryPoint(positions=p, velocities=[1] * self.N_JOINTS, time_from_start=dur)
			dur += rospy.Duration(3)
			self.joint_positions.append(jtp)

		self.jt = JointTrajectory(joint_names=self.names, points=self.joint_positions)
		self.goal = FollowJointTrajectoryGoal(trajectory = self.jt, goal_time_tolerance=dur + rospy.Duration(2))

		self.pub.publish(0)



	def callback(self, data):
		print "This WORKED!!"
		#self.client.wait_for_server()
		#print self.goal
		#self.client.send_goal(self.goal)

		#self.client.wait_for_result()
		#print self.client.get_result()

	def listener(self):
		global callback
		rospy.init_node('listener', anonymous=True)

		rospy.Subscriber("sortmaster", String, callback)
		rospy.spin()


roboXCoord = 0
roboYCoord = 0
roboZCoord = 0


# def callback(data):
# 	global roboXCoord
# 	global roboYCoord
# 	global roboZCoord
# 	x, y, field = data.data.split(",")
#
# 	xCoord = float(x)
# 	yCoord = float(y)
#
# 	coords = [xCoord, yCoord, 6.00]
#
# 	aquiredCoords = CC.CrustInvKin(coords)
#
# 	roboXCoord = aquiredCoords[0]
# 	roboYCoord = aquiredCoords[1]
# 	roboZCoord = aquiredCoords[2]
#
# 	node = ActionExampleNode("/arm_controller/follow_joint_trajectory")
#
# 	node.send_command()






if __name__ == '__main__':
	listener()