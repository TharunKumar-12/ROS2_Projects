import rclpy
from rclpy.node import Node
from bumperbot_msgs.srv import AddTwoInts

class simpleServiceServer(Node):
    def __init__(self):
        super().__init__("simple_service_server")

        self.service_=self.create_service(AddTwoInts,"add_two_ints",self.callBack)

        self.get_logger().info("Starting server")
    def callBack(self,req,res):
        res.sum=req.a+req.b
        return res

def main():
    rclpy.init()
    s=simpleServiceServer()
    rclpy.spin(s)
    s.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
