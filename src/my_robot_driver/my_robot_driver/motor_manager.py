import rclpy
from rclpy.node import Node

class MotorManager(Node):
    def __init__(self):
        super().__init__('motor_manager_node')
        
        # 1. DÉCLARATION DES PARAMÈTRES
        # On définit le nom du paramètre et une valeur par défaut (au cas où le YAML manque)
        self.declare_parameter('serial_port', '/dev/ttyUSB0')
        self.declare_parameter('baudrate', 57600)
        self.declare_parameter('motor_ids', [1])
        self.declare_parameter('loop_rate', 10.0)

        # 2. LECTURE DES PARAMÈTRES (Ceux venant du YAML via le Launch file)
        self.serial_port = self.get_parameter('serial_port').get_parameter_value().string_value
        self.baudrate = self.get_parameter('baudrate').get_parameter_value().integer_value
        self.motor_ids = self.get_parameter('motor_ids').get_parameter_value().integer_array_value
        self.loop_rate = self.get_parameter('loop_rate').get_parameter_value().double_value

        # 3. LOG POUR VÉRIFICATION
        self.get_logger().info('--- Configuration chargée ---')
        self.get_logger().info(f'Port Série : {self.serial_port}')
        self.get_logger().info(f'Baudrate   : {self.baudrate}')
        self.get_logger().info(f'IDs Moteurs: {self.motor_ids}')
        self.get_logger().info(f'Fréquence  : {self.loop_rate} Hz')
        self.get_logger().info('-----------------------------')

        # Ici, on initialisera plus tard la connexion série...

def main(args=None):
    rclpy.init(args=args)
    node = MotorManager()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()