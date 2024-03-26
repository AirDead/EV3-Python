from Core.Core import EV3Controller

if __name__ == "__main__":
    motor_ports = ['A', 'B']
    color_sensor_ports = ['1', '2']

    controller = EV3Controller(motor_ports=motor_ports, color_sensor_ports=color_sensor_ports)

    try:
        while True:
            color = controller.get_color("1")
            print("Цвет:", color)

            controller.move_motor_forward("A", speed=50)
            time.sleep(2)

            controller.stop_motor("A")
            time.sleep(1)

            controller.move_motor_backward("B", speed=30)
            time.sleep(1)

            controller.stop_motor("B")
            time.sleep(1)

    except KeyboardInterrupt:
        for motor_port in motor_ports:
            controller.stop_motor(motor_port)
