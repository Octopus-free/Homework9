from re import findall


class CheckingCard:

    def check_human_players(self, players_count):
        players_count += 1
        for element in range(1, players_count):
            if len(findall(r'[\d]', element)) == 0:
                print(f'Игрок {element} победил!')

    def check_computer_players(self, players_count):
        players_count += 1
        for element in range(1, players_count):
            if len(findall(r'[\d]', element)) == 0:
                print(f'Компьютер {element} победил!')

    def strike_numbers(self, barrel_number, players_cards):

        if barrel_number < 10:
            for card in players_cards:
                if ' {} '.format(barrel_number) in players_cards[card]:
                    players_cards[card] = players_cards[card].replace(' {} '.format(barrel_number), ' - ')
                else:
                    print('Вы проиграли, выпавшего бочонка нет на вашей карточке!')
                    exit(0)
        else:
            for card in players_cards:
                if f' {barrel_number}' in players_cards:
                    players_cards[card] = players_cards[card].replace(str(barrel_number), '--')
                else:
                    print('Вы проиграли, выпавшего бочонка нет на вашей карточке!')
                    exit(0)