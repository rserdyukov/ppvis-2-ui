class Model:
    def __init__(self):
        self.buttons = []
        self.switch = True
        self.coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
            (0, 4, 8), (2, 4, 6),  # D
        )

    def change_buttons(self):
        for button in self.buttons:
            button.color = [0, 0, 0, 1]
            button.text = ""
            button.disabled = False

    def change_disabled(self):
        for button in self.buttons:
            button.disabled = True
