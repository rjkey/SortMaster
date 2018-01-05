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

class RobotMover():
    N_JOINTS = 4

    def MoveTheRobot(self, coords):
        self.joint_positions = []
        self.names = ["joint1", "joint2", "joint3", "joint4"]

        dur = rospy.Duration(2)


