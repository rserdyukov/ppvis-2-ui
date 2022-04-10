from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")

class Model:
    def __init__(self):
        self.coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
            (0, 4, 8), (2, 4, 6),  # D
        )
        self.items = ['']*9
        self.switch = True

    def click(self, index):
        self.items[index] = 'X' if self.switch else 'O'
        self.switch = not self.switch

    def getItems(self):
        return self.items

    def restart(self):
        self.items = [''] * 9
        self.switch = True

    def tic_tac_toe(self):
        vector = lambda item: [self.items[x] for x in item]

        for item in self.coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                return item


class Presenter:
    def __init__(self):
        self.model = Model()

    def click(self, index):
        self.model.click(index)

    def getItems(self):
        return self.model.items

    def restart(self):
        self.model.restart()

    def tic_tac_toe(self):
        return self.model.tic_tac_toe()


class View(BoxLayout):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.controller = Presenter()

        self.orientation = "vertical"
        self.padding = 5

        grid = GridLayout(cols=3)
        for _ in range(9):
            button = Button(
                color=[0, 0, 0, 1],
                font_size=24,
                disabled=False,
                on_press=self.click
            )
            self.buttons.append(button)
            grid.add_widget(button)

        self.add_widget(grid)

        self.add_widget(
            Button(
                text="Restart",
                size_hint=[1, .1],
                on_press=self.restart
            )
        )

    def click(self, arg):
        arg.disabled = True
        self.controller.click(self.buttons.index(arg))
        arg.text = self.controller.getItems()[self.buttons.index(arg)]

        color = [0, 1, 0, 1]

        item = self.controller.tic_tac_toe()
        if item is not None:
            for i in item:
                self.buttons[i].color = color
            for button in self.buttons:
                button.disabled = True

    def restart(self, arg):
        self.controller.restart()

        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""
            button.disabled = False


class TicTackToe(App):
    def __init__(self):
        super().__init__()

    def build(self):
        self.title = "Tic Tack Toe"
        view = View()
        return view


if __name__ == "__main__":
    TicTackToe().run()