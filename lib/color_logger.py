from ev3dev2.sensor.lego import ColorSensor
from importlib import import_module
import os

class ColorLogger:
    def __init__(self):
        self.color_sensor = ColorSensor()

    def check_color(self):
        color = self.color_sensor.color
        try:
            cog_module = import_module(f"cogs.{color}_cog")
            cog = getattr(cog_module, f"{color.capitalize()}Cog")()
            cog.perform_actions()
        except (ModuleNotFoundError, AttributeError):
            print(f"Ког для цвета {color} не найден")

    def load_all_cogs(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith("_cog.py"):
                cog_name = filename[:-7]  # Удаляем "_cog.py" из имени файла
                try:
                    cog_module = import_module(f"cogs.{cog_name}")
                    cog = getattr(cog_module, f"{cog_name.capitalize()}Cog")()
                    self.register_cog(cog_name, cog)
                except (ModuleNotFoundError, AttributeError):
                    print(f"Не удалось загрузить ког {cog_name}")

    def register_cog(self, cog_name, cog_instance):
        # Регистрация кога (этот метод нужно реализовать в соответствии с вашими потребностями)
        pass
