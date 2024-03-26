class ColorActions:
    def __init__(self, color):
        self.color = color

    def perform_actions(self):
        if self.color == 'black':
            self.black_actions()
        elif self.color == 'white':
            self.white_actions()
        else:
            print("Для этого цвета действия не определены")

    def black_actions(self):
        print("Выполняются действия для черного цвета")

    def white_actions(self):
        print("Выполняются действия для белого цвета")
