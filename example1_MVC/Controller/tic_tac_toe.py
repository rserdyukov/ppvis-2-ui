from View.tic_tac_toe import TicTackToeView


class TicTackToeController:
    def __init__(self, model):
        self.model = model
        self.view = TicTackToeView(self)
        self.share_buttons()

    def restart(self, arg):
        self.model.restart(arg)

    def share_buttons(self):
        self.model.buttons = self.view.buttons

    def get_screen(self):
        return self.view.build()

    def tic_tac_toe(self, arg):
        self.model.tic_tac_toe(arg)
