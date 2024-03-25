#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, ColorSensor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds


color = ColorSensor(INPUT_1)

print(color.color)

print(color.reflected_light_intensity)

print(color.rgb)

# Установить датчик в режим RGB
color_sensor.mode = ColorSensor.MODE_RGB_RAW

# Прочитать RGB значения в режиме RAW
rgb_values_raw = color_sensor.raw
print("RGB значения (RAW):", rgb_values_raw)


