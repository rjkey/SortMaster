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
from MoveRobot import RobotMover

from std_msgs.msg import String
from std_msgs.msg import Float64

CC = Calculations()
RobotMover = RobotMover()

class RobotController:

	N_JOINTS = 4
	def __init__(self):
		rospy.init_node('robotcontroller', anonymous=True)

		rospy.Subscriber("sortmaster", String, self.callback)
		self.client = actionlib.SimpleActionClient("/arm_controller/follow_joint_trajectory",
												   FollowJointTrajectoryAction)
		self.gripperPublisher = rospy.Publisher("/gripper/command", Float64)
		self.donePub = rospy.Publisher("robotdone", String)

		rospy.spin()

	def callback(self, data):

		self.client.wait_for_server()
		x, y, field = data.data.split(",")

		# doneArray = [0,0,54.2]
        #
		# self.goal = RobotMover.MoveTheRobot(doneArray)
        #
		# self.client.send_goal(self.goal)
		# self.client.wait_for_result()

		coordArray = [x, y, 4]

		self.gripperPublisher.publish(0)

		rospy.sleep(1)

		self.goal = RobotMover.MoveTheRobot(coordArray)

		self.client.send_goal(self.goal)
		self.client.wait_for_result()

		rospy.sleep(1)

		self.gripperPublisher.publish(1)

		rospy.sleep(1)

		fieldCoord = []

		doneArray = [15,10,30]

		self.goal = RobotMover.MoveTheRobot(doneArray)

		self.client.send_goal(self.goal)
		self.client.wait_for_result()

		if field == "1":
			fieldCoord = [27,7, 7]
		elif field == "2":
			fieldCoord = [27,-7,7]
		elif field == "3":
			fieldCoord = [15,7, 7]
		elif field == "4":
			fieldCoord = [15, -7, 7]

		self.goal = RobotMover.MoveTheRobot(fieldCoord)
		self.client.send_goal(self.goal)
		self.client.wait_for_result()

		rospy.sleep(1)

		self.gripperPublisher.publish(0)

		rospy.sleep(1)

		doneArray = [0,0,54.2]

		self.goal = RobotMover.MoveTheRobot(doneArray)

		self.client.send_goal(self.goal)
		self.client.wait_for_result()

		self.donePub.publish("Done")


if __name__ == '__main__':
	node = RobotController()