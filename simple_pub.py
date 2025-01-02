import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class simplePublisher(Node):
    def __init__(self):
        super().__init__("simplePub")

        self.pub= self.create_publisher(String,"chatter",10)

        self.counter=0
        self.freq=2.0
        self.get_logger().info("Publishing at %d Hz"%self.freq)

        self.timer_=self.create_timer(self.freq,self.callback)
    
    def callback(self):
        msg = String()
        msg.data = "Vanakkam da mapla %d"%self.counter
        self.pub.publish(msg)
        self.counter+=1


def main():
    rclpy.init()
    pub=simplePublisher()
    rclpy.spin(pub)
    pub.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()