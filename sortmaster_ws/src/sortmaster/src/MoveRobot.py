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
        floatXCoord = float(coords[0])
        floatYCoord = float(coords[1])
        floatZCoord = float(coords[2])

        floatCoords = [floatXCoord, floatYCoord, floatZCoord]

        invCoords = CC.CrustInvKin(floatCoords)

        xCoord = invCoords[0]
        yCoord = invCoords[1]
        zCoord = invCoords[2]

        joint_positions = [[xCoord, yCoord, zCoord, 0]]

        dur = rospy.Duration(1.5)

        for p in joint_positions:
            jtp = JointTrajectoryPoint(positions=p, velocities=[1] * self.N_JOINTS, time_from_start=dur)
            dur+=rospy.Duration(2)
            self.joint_positions.append(jtp)

        self.jt = JointTrajectory(joint_names=self.names, points=self.joint_positions)
        self.goal = FollowJointTrajectoryGoal(trajectory = self.jt, goal_time_tolerance=dur + rospy.Duration(2))

        return self.goal



