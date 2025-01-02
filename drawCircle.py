#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class Circle(Node):

    def __init__(self):
        super().__init__("drawCircle")
        self.cmdVelPub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.timer=self.create_timer(1.0,self.sendVel)
        
        print("circle node started.")

    def sendVel(self):
        msg= Twist()
        msg.linear.x=2.0
        msg.angular.z=1.0
        
        self.cmdVelPub.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node=Circle()
    rclpy.spin(node)
    rclpy.shutdown()



