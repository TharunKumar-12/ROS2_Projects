#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import TwistStamped
import numpy as np

class simpleController(Node):
    def __init__(self):
        super().__init__("simple_controller")

        self.declare_parameter("wheel_radius",0.033)
        self.declare_parameter("wheel_separation",0.17)

        self.wheel_rad=self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_sep=self.get_parameter("wheel_separation").get_parameter_value().double_value

        self.get_logger().info("Using wheel radius as %f and wheel separation as %f"%(self.wheel_rad,self.wheel_sep))

        self.wheel_cmd_pub=self.create_publisher(Float64MultiArray,"simple_velocity_controller/commands",10)
        self.vel_sub=self.create_subscription(TwistStamped,"bumperbot_controller/cmd_vel",self.callBack,10)

        self.speed_conversion=np.array([[self.wheel_rad/2,self.wheel_rad/2],
                                [self.wheel_rad/self.wheel_sep,-self.wheel_rad/self.wheel_sep]])

        self.get_logger().info("Speed conversion matrix %s"%self.speed_conversion)

    def callBack(self,msg):
        robot_speed=np.array([[msg.twist.linear.x],
                              [msg.twist.angular.z]])

        wheel_speed=np.matmul(np.linalg.inv(self.speed_conversion),robot_speed)
        wheel_speed_msg=Float64MultiArray()
        wheel_speed_msg.data=[wheel_speed[1,0],wheel_speed[0,0]]
        self.wheel_cmd_pub.publish(wheel_speed_msg)

def main():
    rclpy.init()
    simple_ctrler=simpleController()
    rclpy.spin(simple_ctrler)
    simple_ctrler.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

