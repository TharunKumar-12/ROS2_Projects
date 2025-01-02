#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
class poseSub(Node):

    def __init__(self):
        super().__init__("poseSub")
        self.poseSub=self.create_subscription(Pose,"/turtle1/pose",self.poseCB,10)
    
    def poseCB(self,msg:Pose):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node=poseSub()
    rclpy.spin(node)
    rclpy.shutdown()