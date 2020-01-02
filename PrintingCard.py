# создаем класс для отрисовки в терминале карточек игроков
class PrintingCard:

    # функция для отрисовки карточек игроков людей
    def print_human_cards(self, human_number, human_card):

        print(f'Карточка игрока {human_number} ')
        print('--' * 13)
        print(human_card)
        print('--' * 13)

    # функция для отрисовки карточек игроков компьютеров
    def print_computers_cards(self, computers_players_cards):

        for computer_card in computers_players_cards:
            computer_number = computers_players_cards.index(computer_card) + 1
            print(f'Карточка компьютерного игрока {computer_number} ')
            print('--' * 13)
            print(computer_card)
            print('--' * 13)
