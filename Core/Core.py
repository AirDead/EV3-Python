import time
from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import ColorSensor

class EV3Controller:
    def __init__(self, motor_ports=None, color_sensor_ports=None):
        self.motors = {port: LargeMotor(port) for port in motor_ports if port and port.isalpha()}
        self.color_sensors = {port: ColorSensor(port) for port in color_sensor_ports if port and port.isdigit()}

    def move_motor_forward(self, motor_port, speed=50):
        if motor_port in self.motors:
            self.motors[motor_port].on(speed=speed)

    def move_motor_backward(self, motor_port, speed=50):
        if motor_port in self.motors:
            self.motors[motor_port].on(speed=-speed)

    def stop_motor(self, motor_port):
        if motor_port in self.motors:
            self.motors[motor_port].off()

    def get_color(self, color_sensor_port):
        if color_sensor_port in self.color_sensors:
            return self.color_sensors[color_sensor_port].color
        else:
            return None
