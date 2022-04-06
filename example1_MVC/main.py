"""Дюбайло Матвей гр.021704"""
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class TicTackToeView(App):
    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.controller = controller
        self.buttons = []
        self.gr = self.build_buttons()

    def build_buttons(self):
        grid = GridLayout(cols=3)
        for _ in range(9):
            button = Button(
                color=[0, 0, 0, 1],
                font_size=24,
                disabled=False,
                on_press=self.tic_tac_toe
            )
            self.buttons.append(button)
            grid.add_widget(button)
        return grid

    def build(self):
        self.title = "Tic Tack Toe"
        root = BoxLayout(orientation="vertical", padding=5)
        root.add_widget(self.gr)
        root.add_widget(
            Button(
                text="Restart",
                size_hint=[1, .1],
                on_press=self.restart
            )
        )
        return root

    def tic_tac_toe(self, arg):
        arg.text = self.controller.tic_tac_toe(arg)
        flag_win, item_color = self.controller.check_win()
        if flag_win:
            color = [0, 1, 0, 1]
            for i in item_color:
                self.buttons[i].color = color

    def restart(self, arg):
        self.controller.restart(arg)
        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""


class TicTackToeModel:
    def __init__(self):
        self.buttons = []
        self.switch = True

    def tic_tac_toe(self, arg):
        arg.disabled = True
        text = 'X' if self.switch else 'O'
        self.switch = not self.switch
        return text

    def check_win(self):
        coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
            (0, 4, 8), (2, 4, 6),  # D
        )

        vector = lambda item: [self.buttons[x].text for x in item]

        for item in coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for button in self.buttons:
                    button.disabled = True
                return win, item

        return False, None

    def restart(self, arg):
        self.switch = True
        for button in self.buttons:
            button.disabled = False


class TicTackToeController:
    def __init__(self, model):
        self.model = model
        self.view = TicTackToeView(self)
        self.share_buttons()

    def tic_tac_toe(self, arg):
        return self.model.tic_tac_toe(arg)

    def share_buttons(self):
        self.model.buttons = self.view.buttons

    def get_screen(self):
        return self.view.build()

    def check_win(self):
        return self.model.check_win()

    def restart(self, arg):
        self.model.restart(arg)


class PassMVC(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = TicTackToeModel()
        self.controller = TicTackToeController(model=self.model)

    def build(self):
        return self.controller.get_screen()


PassMVC().run()
