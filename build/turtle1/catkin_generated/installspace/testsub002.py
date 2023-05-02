#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
from turtlesim.msg import Pose

def doPose(data):
    rospy.loginfo("乌龟坐标:x=%.2f, y=%.2f,theta=%.2f",data.x,data.y,data.theta)

if __name__ == "__main__":

   
    rospy.init_node("sub_pose_p")

   
    sub = rospy.Subscriber("/turtle1/pose",Pose,doPose,queue_size=1000)
    
    rospy.spin()
