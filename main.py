#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

color_sensor = ColorSensor()

print("Color:", color_sensor.color)
print("Reflected light intensity:", color_sensor.reflected_light_intensity)
print("RGB:", color_sensor.rgb)

color_sensor.mode = ColorSensor.MODE_RGB_RAW

rgb_values_raw = color_sensor.raw
print("RGB values (RAW):", rgb_values_raw)
