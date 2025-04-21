
import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class MinimalPublisher(Node):


    def __init__(self):
        super().__init__('minimal_publisher')

        self.publisher_ = self.create_publisher(Twist, '/diff_drive/cmd_vel', 10)
        self.subscription = self.create_subscription(LaserScan, '/diff_drive/scan', self.timer_callback, 10)
        self.prevLeft = 0.0


    def timer_callback(self, msginfo):

        msg = Twist()

        if self.prevLeft == 0.0:
            self.prevLeft = msginfo.ranges[1]

        if msginfo.ranges[0] < 5.0:
            msg.linear.x = 0.0
            msg.angular.z = -1.0
        elif (msginfo.ranges[2] > self.prevLeft) and (msginfo.ranges[0] > 5.0) and (msginfo.ranges[1] > 5.0):
            msg.linear.x = 0.0
            msg.angular.z = 0.5
        else:
            msg.linear.x = 2.0
            msg.angular.z = 0.0

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
