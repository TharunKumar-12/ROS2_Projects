#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial

class turtleControl(Node):
    
   
    def __init__(self):
        super().__init__("turtleControl")
        self.previousX=0
        self.poseSub = self.create_subscription(Pose,"/turtle1/pose",self.poseSubCB,10)
        self.posePub = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.get_logger().info("Turtle controller started")
        
    def posePubCB(self,a,v):
        vel= Twist()
        
        vel.linear.x=v
        vel.angular.z=a
        self.posePub.publish(vel)

    def poseSubCB(self ,pose: Pose):
        if (pose.x < 9.0 and pose.x>2.0) and (pose.y < 9.0 and pose.y>2.0):
            self.posePubCB(0.0,2.0)
        elif (pose.x >= 8.0 or pose.y >=8.0) or (pose.x <=2.0 or pose.y <=2.0):
            
            self.posePubCB(0.9 , 1.0)
        else:
            self.posePubCB(0.0,-1.0)

        if pose.x > 5.5 and self.previousX<=5.5:
            self.previousX=pose.x
            self.callSetPen(255,0,0,3,0)
        elif pose.x <=5.5 and self.previousX>5.5:
            self.previousX=pose.x
            self.callSetPen(0,255,0,3,0)
    def callSetPen(self, r, g, b, width, off):
        client=self.create_client(SetPen,"/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service...")
        
        request = SetPen.Request()
        request.r =r
        request.g = g
        request.b = b 
        request.width= width
        request.off=off

        future= client.call_async(request)
        future.add_done_callback(partial(self.callBackSetPen))
    def callBackSetPen(self,future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %r" % (e,))



def main(args=None):
    rclpy.init(args=args)
    node=turtleControl()
    rclpy.spin(node)
    rclpy.shutdown()