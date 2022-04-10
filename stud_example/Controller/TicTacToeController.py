"""Белик Сергей гр.021702"""
from stud_example.Model.TicTacToeModel import TicTackToeModel
from stud_example.View.TicTacToeView import TicTackToeView


class TicTacToeController:
    def __init__(self):
        self.model = TicTackToeModel()
        self.view = TicTackToeView(self)

    def tic_tac_toe(self, instance):
        self.model.tic_tac_toe(instance)

    def restart(self):
        self.model.restart()


if __name__ == "__main__":
    Example = TicTacToeController()
    Example.view.run()
