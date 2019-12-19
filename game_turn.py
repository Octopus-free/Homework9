from card_for_game import HandfulGeneration


class NextTurn:

    def __init__(self):
        self.turn_number = 1

    def turn(self):
        self.turn_number += 1
        return self.turn_number

