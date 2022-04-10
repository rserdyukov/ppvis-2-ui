from kivy.app import App
from example2.model.toe_model import Model


class Controller(App, Model):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def restart(self):
        self.switch = True
        self.change_buttons()

    def tic_tac_toe(self, arg):
        arg.disabled = True
        arg.text = 'X' if self.switch else 'O'
        self.switch = not self.switch

        vector = lambda item: [self.buttons[x].text for x in item]

        for item in self.coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                for i in item:
                    self.buttons[i].color = [0, 1, 0, 1]
                for button in self.buttons:
                    button.disabled = True
                break
