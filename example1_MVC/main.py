"""Дюбайло Матвей гр.021704"""
from kivy.app import App
from Controller.tic_tac_toe import TicTackToeController
from Model.tic_tac_toe import TicTackToeModel
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class PassMVC(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = TicTackToeModel()
        self.controller = TicTackToeController(model=self.model)

    def build(self):
        return self.controller.get_screen()


PassMVC().run()
