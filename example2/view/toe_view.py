from kivy.lang import Builder
from kivy.config import Config
from example2.controller.toe_controller import Controller

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class TicTackToeView(Controller):
    def __init__(self):
        super().__init__()
        self.controller = Controller()

    def build(self):
        self.title = "Tic Tack Toe"
        root = Builder.load_file('view/tic_tac_toe.kv')
        self.controller.buttons = [b for b in root.ids.values()]
        return root
