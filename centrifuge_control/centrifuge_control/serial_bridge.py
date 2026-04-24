#!/usr/bin/env python3

# ===== Imports =====
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial

class SerialBridge(Node):
    def __init__(self):
        super().__init__('serial_bridge')

        self.subscription = self.create_subscription(
            Int32,
            'centrifuge_cmd',
            self.command_callback,
            10
        )

        # CHANGE THIS if needed
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

        self.get_logger().info("Serial bridge connected to Arduino")

    def command_callback(self, msg):
        cmd = f"{msg.data}\n"
        self.ser.write(cmd.encode('utf-8'))
        self.get_logger().info(f"Sent to Arduino: {cmd.strip()}")

def main():
    rclpy.init()
    node = SerialBridge()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.ser.close()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()