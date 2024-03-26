from Core.Core import EV3Controller

# Получите порты моторов и цветовых датчиков из какого-то источника, например, из файла, конфигурации и т.д.
motor_ports = ['outA', 'outB']
color_sensor_ports = ['1', '2']

# Создайте экземпляр контроллера EV3, передав список портов
controller = EV3Controller(motor_ports=motor_ports, color_sensor_ports=color_sensor_ports)

# Теперь вы можете использовать функции контроллера, например:
controller.move_forward()
