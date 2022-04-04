from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


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
                on_press=self.controller.tic_tac_toe
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
                on_press=self.controller.restart
            )
        )
        return root
