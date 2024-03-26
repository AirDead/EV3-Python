import time
from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import ColorSensor

class EV3Controller:
    def __init__(self, motor_ports=None, color_sensor_ports=None):
        self.motors = [LargeMotor(port) for port in motor_ports if port and port.isalpha()]
        self.color_sensors = [ColorSensor(port) for port in color_sensor_ports if port and port.isdigit()]

    def move_forward(self, speed=50):
        for motor in self.motors:
            motor.on(speed=speed)

    def move_backward(self, speed=50):
        for motor in self.motors:
            motor.on(speed=-speed)

    def stop_motors(self):
        for motor in self.motors:
            motor.off()

    def get_colors(self):
        return [sensor.color for sensor in self.color_sensors]
