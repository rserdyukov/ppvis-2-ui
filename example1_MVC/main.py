"""Дюбайло Матвей гр.021704"""
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class TicTackToeView:
    def __init__(self, model, **kw):
        super().__init__(**kw)
        self.model = model
        self.buttons = self.model.buttons

    def build(self):
        root = BoxLayout(orientation="vertical", padding=5)
        grid = GridLayout(cols=3)
        for button in self.buttons['map']:
            grid.add_widget(button)
        root.add_widget(grid)
        root.add_widget(self.buttons['restart'])
        return root

    def tic_tac_toe(self, flag_win, item_color):
        if flag_win:
            color = [0, 1, 0, 1]
            for i in item_color:
                self.buttons['map'][i].color = color

    def restart(self, arg):
        for button in self.buttons['map']:
            button.color = [0, 0, 0, 1]
            button.text = ""

    def cell_changes(self, arg, text):
        arg.text = text


class TicTackToeModel:
    def __init__(self, controller):
        self.buttons = {}
        self.switch = True
        self.controller = controller

    def build_buttons(self):
        buttons = []
        for _ in range(9):
            button = Button(
                color=[0, 0, 0, 1],
                font_size=24,
                disabled=False,
                on_press=self.controller.tic_tac_toe
            )
            buttons.append(button)
        self.buttons['map'] = buttons
        self.buttons['restart'] = Button(
            text="Restart",
            size_hint=[1, .1],
            on_press=self.controller.restart
        )

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

        vector = lambda item: [self.buttons['map'][x].text for x in item]

        for item in coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                win = True
                for button in self.buttons['map']:
                    button.disabled = True
                return win, item

        return False, None

    def restart(self, arg):
        self.switch = True
        for button in self.buttons['map']:
            button.disabled = False


class TicTackToeController:
    def __init__(self):
        self.model = TicTackToeModel(self)
        self.view = TicTackToeView(self.model)

    def tic_tac_toe(self, arg):
        text = self.model.tic_tac_toe(arg)
        self.view.cell_changes(arg, text)
        flag_win, item_color = self.model.check_win()
        self.view.tic_tac_toe(flag_win, item_color)

    def get_buttons(self):
        return self.model.buttons

    def get_screen(self):
        self.model.build_buttons()
        return self.view.build()

    def restart(self, arg):
        self.model.restart(arg)
        self.view.restart(arg)


class PassMVC(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = TicTackToeController()

    def build(self):
        self.title = "Tic Tack Toe"
        return self.controller.get_screen()


PassMVC().run()
