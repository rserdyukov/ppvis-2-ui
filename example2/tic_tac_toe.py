from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class TicTackToe(App):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.switch = True

    def tic_tac_toe(self, arg):
        arg.disabled = True
        arg.text = 'X' if self.switch else 'O'
        self.switch = not self.switch

        coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
            (0, 4, 8), (2, 4, 6),  # D
        )

        vector = lambda item: [self.buttons[x].text for x in item]

        color = [0, 1, 0, 1]

        for item in coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for i in item:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                break

    def restart(self):
        self.switch = True

        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""
            button.disabled = False

    def build(self):
        self.title = "Tic Tack Toe"
        root = Builder.load_file('tic_tac_toe.kv')
        self.buttons = [b for b in root.ids.values()]
        return root


if __name__ == "__main__":
    TicTackToe().run()