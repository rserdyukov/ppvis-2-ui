from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")

load_file = Builder.load_string('''
BoxLayout:
    orientation: "vertical"
    padding: 5

    GridLayout:
        cols: 3

        Button:
            id: btn1
            color: 0, 0, 0, 1
            text: ""
            font_size: 24
            disabled: False
            on_press: app.controller.tic_tac_toe(btn1)

        Button:
            id: btn2
            color: 0, 0, 0, 1
            text: ""
            font_size: 24
            disabled: False
            on_press: app.controller.tic_tac_toe(btn2)

        Button:
            id: btn3
            color: 0, 0, 0, 1
            text: ""
            font_size: 24
            disabled: False
            on_press: app.controller.tic_tac_toe(btn3)

        Button:
            id: btn4
            color: 0, 0, 0, 1
            text: ""
            font_size: 24
            disabled: False
            on_press: app.controller.tic_tac_toe(btn4)

        Button:
            id: btn5
            color: 0, 0, 0, 1
            text: ""
            font_size: 24
            disabled: False
            on_press: app.controller.tic_tac_toe(btn5)

        Button:
            id: btn6
            color: 0, 0, 0, 1
            text: ""
            font_size: 24
            disabled: False
            on_press: app.controller.tic_tac_toe(btn6)

        Button:
            id: btn7
            color: 0, 0, 0, 1
            text: ""
            font_size: 24
            disabled: False
            on_press: app.controller.tic_tac_toe(btn7)

        Button:
            id: btn8
            color: 0, 0, 0, 1
            text: ""
            font_size: 24
            disabled: False
            on_press: app.controller.tic_tac_toe(btn8)

        Button:
            id: btn9
            color: 0, 0, 0, 1
            text: ""
            font_size: 24
            disabled: False
            on_press: app.controller.tic_tac_toe(btn9)

    Button:
        text: "Restart"
        size_hint: 1, .1
        on_press: app.controller.restart()
''')


class TicTackToeView(App):
    def __init__(self, controller):
        super(TicTackToeView, self).__init__()
        self.controller = controller
        self.buttons = []

    def build(self):
        self.title = "Tic Tack Toe"
        root = load_file
        self.buttons = [b for b in root.ids.values()]
        self.controller.model.buttons = self.buttons
        return root
