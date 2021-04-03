#!/usr/bin/env python
# written by Hariharan <A.H.N>
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32


def callback(msg):
    print msg.data
    twist = Twist()
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    if 10 >= msg.data >= 0:
        twist.linear.x = 0
        twist.angular.z = 0.5
    elif 20 >= msg.data > 10:
        twist.linear.x = 0.5
        twist.angular.z = 0
    elif 30 >= msg.data > 20:
        twist.linear.x = 0
        twist.angular.z = -0.5
    elif 40 >= msg.data > 30:
        twist.linear.x = -0.5
        twist.angular.z = 0
    else:
        twist.linear.x = 0
        twist.angular.z = 0

    pub.publish(twist)


if __name__ == "__main__":
    rospy.init_node('sensor_decode')
    sub = rospy.Subscriber('sensor', Float32, callback)
    rospy.spin()
