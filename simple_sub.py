import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class simpleSubcriber(Node):
    def __init__(self):
        super().__init__("simpleSubsriber")
        self.sub=self.create_subscription(String,"chatter",self.callBack,10)
    def callBack(self,msg:String):
        self.get_logger().info(msg.data)

def main():
    rclpy.init()
    sub=simpleSubcriber()
    rclpy.spin(sub)
    sub.destroy_node()
    rclpy.shutdown()

