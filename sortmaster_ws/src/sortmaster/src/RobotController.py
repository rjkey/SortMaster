#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    x, y, field = data.data.split(",")
    rospy.loginfo(rospy.get_caller_id() + "1 - I heard %s", x)
    rospy.loginfo(rospy.get_caller_id() + "2 - I heard %s", y)
    rospy.loginfo(rospy.get_caller_id() + "3 - I heard %s", field)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("sortmaster", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()