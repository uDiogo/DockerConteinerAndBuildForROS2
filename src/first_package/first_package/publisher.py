
#rclpy é  uma API em python para comunicação e interação com ROS 2.

import rclpy

from std_msgs.msg import String

from rclpy.node import Node

#cria um classe que esta ligada ao rclpy.Node
class PublisherNode(Node):
    def __init__(self):
        #chamamos o contrutor parente da class rclpy.Node
        #e especificamos o nome, como o construtor super, nos herdamos a classe importada para ca
        super().__init__('node_publisher')

        #agora temos que declarar que o nosso no ira publicar menssagens 
        #com um topico chamado 'communication_topic'
        #o nome do topico deve ser compativel com o nome inscrito no arquivo Python
        #o ultimo argumento é o tamanho do buffer de menssagens

        self.publisher_ = self.create_publisher(String, 'communication_topic', 15)
        #criamos o tempo entre as comunicações
        commRate = 1

        #setamos o timer
        #esse timer ira chamar a função self.callbackFunction definida acima com 1 seg de rate
        self.timer = self.create_timer(commRate, self.callbackFunction)
        #counter
        self.counter = 0


        #criando um função que e executada pelo tempo
    def callbackFunction(self):
        menssagePublisher = String()
        #populamos a messagem com uma String
        menssagePublisher.data = 'Counter value: %d' % self.counter
        #publish the message to the topic
        self.publisher_.publish(menssagePublisher)
        #publicamos a messagem que ira aparecer na janela que o no foi publicado
        self.get_logger().info('Publisher node is publishing: "%s" ' % menssagePublisher.data)
        #incrementamos o contador
        self.counter=self.counter+1

def main(args = None):
    rclpy.init(args=args)
    node_publisher = PublisherNode()
    rclpy.spin(node_publisher)
    node_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()