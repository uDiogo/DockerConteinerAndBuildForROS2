import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class SubscriberNode(Node):
    
    def __init__(self):
        # chamamos o construtor parente da class rclpy.Node
        # e especificamos o nome, como o construtor super, nos herdamos a classe importada para ca
        super().__init__('node_subscriber')

        self.subscription = self.create_subscription(
            String, 
            'communication_topic', 
            self.callbackFunction, 
            15)
        


    def callbackFunction(self, message):
        self.get_logger().info('We received "%s"' % message.data)


def main(args = None):
    rclpy.init(args=args)
    node_subscriber = SubscriberNode()
    rclpy.spin(node_subscriber)
    node_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()