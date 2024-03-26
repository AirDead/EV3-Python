from Core.Core import EV3Controller

motor_ports = ['outA', 'outB']
color_sensor_ports = ['1', '2']
controller = EV3Controller(motor_ports=motor_ports, color_sensor_ports=color_sensor_ports)

controller.move_forward()
