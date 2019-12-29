from card_for_game import HandfulGeneration


class NextTurn:

    def __init__(self):
        self.turn_number = 1

    def turn(self, turn_number):

        turn_message = f'Ход {turn_number}'

        return turn_message

