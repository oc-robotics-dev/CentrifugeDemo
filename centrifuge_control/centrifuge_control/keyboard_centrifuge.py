#!/usr/bin/env python3

# ===== Imports =====
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import sys
import termios
import tty

class KeyboardCentrifuge(Node):
    def __init__(self):
        super().__init__('keyboard_centrifuge')
        self.publisher = self.create_publisher(Int32, 'centrifuge_cmd', 10)

        self.get_logger().info("Keyboard control ready")
        self.get_logger().info("1=ON | 2=OFF | +=increment | -=decrement")

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

    def run(self):
        while rclpy.ok():
            key = self.get_key()
            msg = Int32()

            if key == '1':
                msg.data = 1000        # ON
            elif key == '2':
                msg.data = 1001        # OFF
            elif key == '+':
                msg.data = 1           # increment
            elif key == '-':
                msg.data = -1          # decrement
            else:
                continue

            self.publisher.publish(msg)
            self.get_logger().info(f"Sent command: {msg.data}")

def main():
    rclpy.init()
    node = KeyboardCentrifuge()

    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()